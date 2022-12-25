import task1.password_checker as password_checker
import task1.sum_of_all as sum_of_all
import task1.fibo as fibo


def test_password_checker_password_len():
    assert password_checker.password_checker('abcd') == False

def test_password_checker_digits_count():
    assert password_checker.password_checker('ajdsasasd') == False

def test_password_checker_not_only_digits():
    assert password_checker.password_checker('123421421412') == False

def test_password_checker_if_password_word_in_password():
    assert password_checker.password_checker('PasSword1231') == False

def test_sum_of_all_3_2_1():
    assert sum_of_all.summ_of_all(1,2,3) == 6

def test_sum_of_all_05_016():
    assert sum_of_all.summ_of_all(0.5, 0.16) == 0.66

def test_sum_of_all_nothing():
    assert sum_of_all.summ_of_all() == 0

def test_fibo_32():
    assert fibo.Fibo(32) == 1346269

def test_fibo_1():
    assert fibo.Fibo(1) == 0
