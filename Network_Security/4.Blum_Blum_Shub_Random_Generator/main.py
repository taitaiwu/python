import math


def is_prime(num):
    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0:
        return False
    for i in range(3, math.isqrt(num) + 1, 2):
        if num % i == 0:
            return False
    return True


def validate_bbs_params(p, q, seed):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("p 和 q 必須為質數")
    if p % 4 != 3 or q % 4 != 3:
        raise ValueError("p 和 q 必須滿足 p mod 4 = 3 且 q mod 4 = 3")
    if p == q:
        raise ValueError("p 不可等於 q")
    n = p * q
    if seed <= 1 or math.gcd(seed, n) != 1:
        raise ValueError("seed 必須大於 1 且與 n 互質")
    return n


def bbs_generate(p, q, seed, length):
    n = validate_bbs_params(p, q, seed)
    x = (seed * seed) % n
    bits = []
    for _ in range(length):
        x = (x * x) % n
        bits.append(x & 1)
    return bits


def test1_bit_balance(bits):
    number_of_0 = bits.count(0)
    number_of_1 = bits.count(1)
    passed = 4800 <= number_of_0 <= 5200 and 4800 <= number_of_1 <= 5200
    return {"number_of_0": number_of_0, "number_of_1": number_of_1, "passed": passed}


def test2_max_run(bits):
    max_run = 1
    run = 1
    for prev, cur in zip(bits, bits[1:]):
        if cur == prev:
            run += 1
            max_run = max(max_run, run)
        else:
            run = 1
    return {"max_run_length": max_run, "passed": max_run <= 20}


def test3_block_balance(bits, block_size=100, low=35, high=65, required_pass=95):
    counts = []
    for i in range(0, len(bits), block_size):
        block = bits[i:i + block_size]
        counts.append(sum(block))
    blocks_passed = sum(1 for c in counts if low <= c <= high)
    return {
        "ones_per_block": counts,
        "blocks_passed": blocks_passed,
        "total_blocks": len(counts),
        "passed": blocks_passed >= required_pass,
    }


def test4_pattern_freq(bits, low=1000, high=1500):
    counts = {"00": 0, "01": 0, "10": 0, "11": 0}
    for i in range(0, len(bits) - 1, 2):
        key = f"{bits[i]}{bits[i + 1]}"
        counts[key] += 1
    passed = all(low <= v <= high for v in counts.values())
    return {"pattern_counts": counts, "passed": passed}


def test5_half_match(bits, low=2300, high=2700):
    half = len(bits) // 2
    first_half, second_half = bits[:half], bits[half:]
    same_count = sum(1 for a, b in zip(first_half, second_half) if a == b)
    return {"same_count": same_count, "passed": low <= same_count <= high}


def run_all_tests(bits):
    return {
        "test1": test1_bit_balance(bits),
        "test2": test2_max_run(bits),
        "test3": test3_block_balance(bits),
        "test4": test4_pattern_freq(bits),
        "test5": test5_half_match(bits),
    }


def bits_to_str(bits):
    return "".join(str(b) for b in bits)


def print_report(title, p, q, seed, n_bits, bits, results):
    status = lambda passed: "PASS" if passed else "FAIL"

    print("=" * 60)
    print(title)
    print("=" * 60)
    print(f"p = {p}, q = {q}, seed = {seed}, N = {n_bits}")
    print(f"前 100 bits: {bits_to_str(bits[:100])}")

    t1 = results["test1"]
    print(f"\n[Test 1] 0 的數量 = {t1['number_of_0']}, "
          f"1 的數量 = {t1['number_of_1']} -> {status(t1['passed'])}")

    t2 = results["test2"]
    print(f"[Test 2] 最長連續相同 bit 長度 = {t2['max_run_length']} "
          f"-> {status(t2['passed'])}")

    t3 = results["test3"]
    print(f"[Test 3] 平衡測試通過組數 = {t3['blocks_passed']} / {t3['total_blocks']} "
          f"-> {status(t3['passed'])}")

    t4 = results["test4"]
    pc = t4["pattern_counts"]
    print(f"[Test 4] 00={pc['00']}, 01={pc['01']}, 10={pc['10']}, 11={pc['11']} "
          f"-> {status(t4['passed'])}")

    t5 = results["test5"]
    print(f"[Test 5] same_count = {t5['same_count']} -> {status(t5['passed'])}")

    overall = all(results[k]["passed"] for k in results)
    print(f"\n整體結果: {'全部測試通過' if overall else '有測試未通過'}")
    print()


def main():
    n_bits = 10000

    # 三組參數，用來分析 p, q, seed 對測試結果的影響
    param_sets = [
        {"label": "參數組 1：p=3, q=7, seed=4 (小參數)", "p": 3, "q": 7, "seed": 4},
        {"label": "參數組 2：p=1000003, q=2000003, seed=271828182 (大參數)",
         "p": 1000003, "q": 2000003, "seed": 271828182},
        {"label": "參數組 3：與參數組 2 相同 p, q，不同 seed",
         "p": 1000003, "q": 2000003, "seed": 123456789},
    ]

    output_set_index = 1  # 使用參數組 2 的結果輸出到 bbs_output.txt

    for i, params in enumerate(param_sets):
        bits = bbs_generate(params["p"], params["q"], params["seed"], n_bits)
        results = run_all_tests(bits)
        print_report(params["label"], params["p"], params["q"], params["seed"], n_bits, bits, results)

        if i == output_set_index:
            with open("bbs_output.txt", "w") as f:
                f.write(bits_to_str(bits))
            print(f"已將 {n_bits} bits 輸出至 bbs_output.txt\n")


if __name__ == "__main__":
    main()
