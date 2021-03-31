 Олег получил инвестиции на стартап по машинному обучению, и занимается распознаванием закономерностей в тексте.

Его первый продукт будет анализировать текст, преобразованный из изображений точек и звёздочек, которые рисуют первоклассники в тетрадках. Последовательности всегда составлены по общему шаблону, но первоклассники пока часто ошибаются, и забывают поставить точку, рисуют лишнюю звёздочку, и т. п.

На вход программы поступают строки, состоящие из символов "." и "*", всегда начинающиеся и завершающиеся звёздочкой. В них всегда повторяется единый шаблон, например:

*..*..*..*..*..*..*

Такой пример считается корректным.

Однако первоклассники иногда ошибаются, и могут написать такие ошибочные строки:

*..*...*..*..*..*..*
*..*..*..*..*..**..*

Ещё примеры корректных строк:

*
***
*.......*.......*
**
*.*

Функция

bool LineAnalysis(string line)

получает на вход строку для анализа и возвращает логическое true/false, обозначающее корректность строки. 