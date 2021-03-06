"""
FizzBuzz.

- [x] 数字を文字列で返す
  - [x] 1を渡したら文字列"1"を返す
  - [x] 2を渡したら文字列"2"を返す
ただし、
- [X] 3で割り切れる数の場合は「Fizz」と返す
- [x] 5で割り切れる数の場合は「Buzz」と返す
- [x] 3と5で割り切れる数の場合は「FizzBuzz」と返す

- [x] 7で割り切れる数の場合は「Hoge」と返す
- [x] 3と7で割り切れる数の場合は「FizzHoge」と返す
- [x] 5と7で割り切れる数の場合は「BuzzHoge」と返す
- [x] 3と5と7で割り切れる数の場合は「FizzBuzzHoge」と返す

- [x] リファクタリング
"""
import pytest


def fizz_buzz_hoge(num):
    """FizzBuzzHoge."""
    result = ""
    if num % 3 == 0:
        result += "Fizz"
    if num % 5 == 0:
        result += "Buzz"
    if num % 7 == 0:
        result += "Hoge"
    if result == "":
        result = str(num)
    return result


@pytest.mark.parametrize(['test_input', 'expected'], [
(1, "1"), (2, "2"),
    (3, "Fizz"), (6, "Fizz"),
    (5, "Buzz"), (10, "Buzz"),
    (15, "FizzBuzz"), (30, "FizzBuzz"),
    (7, "Hoge"), (14, "Hoge"),
    (21, "FizzHoge"),
    (35, "BuzzHoge"),
    (105, "FizzBuzzHoge")
])
def test_fizz_buzz_hoge(test_input, expected):
    assert expected == fizz_buzz_hoge(test_input)

# def test_fizzbuzz_1():
#     """1を渡したら文字列1を返すテスト."""
#     assert "1" == fizz_buzz_hoge(1)
#
#
# def test_fizzbuzz_2():
#     """2を渡したら2を返すのを確認するテスト."""
#     assert "2" == fizz_buzz_hoge(2)
#
#
# def test_fizzbuzz_3():
#     """3を渡したらFizzを返すのを確認するテスト."""
#     assert "Fizz" == fizz_buzz_hoge(3)
#
#
# def test_fizzbuzz_6():
#     """6を渡したらFizzを返すのを確認するテスト."""
#     assert "Fizz" == fizz_buzz_hoge(6)
#
#
# def test_fizzbuzz_5():
#     """5を渡したらBuzzを返すのを確認するテスト."""
#     assert "Buzz" == fizz_buzz_hoge(5)
#
#
# def test_fizzbuzz_10():
#     """5を渡したらBuzzを返すのを確認するテスト."""
#     assert "Buzz" == fizz_buzz_hoge(10)
#
#
# def test_fizzbuzz_15():
#     """15を渡したらFizzBuzzを返すのを確認するテスト."""
#     assert "FizzBuzz" == fizz_buzz_hoge(15)
#
#
# def test_fizzbuzz_30():
#     """30を渡したらFizzBuzzを返すのを確認するテスト."""
#     assert "FizzBuzz" == fizz_buzz_hoge(30)
#
#
# def test_fizzbuzz_7():
#     """7を渡したらHogeを返すのを確認するテスト."""
#     assert "Hoge" == fizz_buzz_hoge(7)
#
#
# def test_fizzbuzz_14():
#     """14を渡したらHogeを返すのを確認するテスト."""
#     assert "Hoge" == fizz_buzz_hoge(14)
#
#
# def test_fizzbuzz_21():
#     """21を渡したらFizzHogeを返すのを確認するテスト."""
#     assert "FizzHoge" == fizz_buzz_hoge(21)
#
#
# def test_fizzbuzz_35():
#     """35を渡したらBuzzHogeを返すのを確認するテスト."""
#     assert "BuzzHoge" == fizz_buzz_hoge(35)
#
#
# def test_fizzbuzz_105():
#     """105を渡したらFizzBuzzHogeを返すのを確認するテスト."""
#     assert "FizzBuzzHoge" == fizz_buzz_hoge(105)
