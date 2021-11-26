def sum(a,b):
	return a + b


def test_pass():
	assert True

def test_sum_works_as_expected():
	if sum(1,1) == 2:
		assert True
	else:
		assert False


