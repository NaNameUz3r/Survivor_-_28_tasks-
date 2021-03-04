 Требуется вычислить разницу между двумя целыми неотрицательными числами, заданными своим строковым представлением (например, "1234567890" и "321").
Числа задаются в диапазоне от 0 до 10^16 (включительно).

В некоторых языках есть поддержка так называемых BigInteger, которые потенциально не ограничены диапазонами, однако арифметические операции над ними выполняются не процессором, а эмуляционным кодом. По сути, для этих операций просто вызываются функции стандартных библиотек.

Возможно, в выбранном вами языке имеется поддержка BigInteger, однако в данной миссии надо обойтись без них.
Придумайте, как вычислять разность для любых заданных значений.

Функция

string BigMinus(string s1, string s2)

получает на вход два числа в формате строки (числа всегда корректные -- набор цифр), и возвращает абсолютное значение (модуль) разности -- первое число s1 минус второе число s2, также в формате строки.

Например,
BigMinus("1234567891", "1") = "1234567890"
BigMinus("1", "321") = "320" 