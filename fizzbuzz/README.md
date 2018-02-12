# FizzBuzz

FizzBuzzプログラムとテストを書きます。

FizzBuzzに関してはwikipediaを参照ください。 [Fizz Buzz - Wikipedia](https://ja.wikipedia.org/wiki/Fizz_Buzz)

## 仕様を考える
まずは、Fizz Buzzの仕様を考えます。

数を与えると、その数に応じて戻り値が異なる

- [ ] 3で割り切れる数の場合は「Fizz」と返す
- [ ] 5で割り切れる数の場合は「Buzz」と返す
- [ ] 3と5で割り切れる数の場合は「FizzBuzz」と返す
- [ ] 3でも5でも割り切れない数の場合は、その数をそのまま返す
- [ ] リファクタリング

テスト駆動開発の順序でテストを書く

1. テストを1つ書く

  - [ ] 3で割り切れる数の場合は「Fizz」と返す

2. すべてのテストを走らせ、新しいテストの失敗を確認する
3. 小さな変更を行う
4. すべてのテストを走らせ、すべて成功することを確認する
5. 1に戻る

  - [ ] 5で割り切れる数の場合は「Buzz」と返す
  - [ ] 3と5で割り切れる数の場合は「FizzBuzz」と返す
  - [ ] 3でも5でも割り切れない数の場合は、その数をそのまま返す

6. リファクタリングを行って重複を除去する