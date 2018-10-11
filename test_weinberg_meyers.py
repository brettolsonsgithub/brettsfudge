import itertools, random, string, unittest


class Triangle(object):
    @staticmethod
    def triangle_app(a, b, c):
        # PART1 - input validation
        for x in (a, b, c):
            # type check- make sure a,b,c is an int
            int(x)

            # make sure a,b,c is not negative
            if x < 0:
                raise ValueError('ERROR: parameter {0} is a negative number'.format(x))

            # make sure a,b,c is not single digit, non-zero value
            elif x == 0 or x > 9:
                raise ValueError('ERROR: no parameter value can be = 0 or > 9. You passed in {0}, {1}, {2}'.format(a,b,c))

        # PART2, valid sets - is the sum of any two sides less than or equal to a third?
        # ('a', 'b', 'c')
        # ('a', 'c', 'b')
        # ('b', 'a', 'c')
        # ('b', 'c', 'a')
        # ('c', 'a', 'b')
        # ('c', 'b', 'a')

        for each in itertools.permutations((a, b, c)):
            if each[0] + each[1] < each[2]:
                raise ValueError('ERROR: {0} + {1} < {2} is not a triangle'.format(a,b,c))

            if each[0] + each[1] == each[2]:
                raise ValueError('ERROR: {0} + {1} == {2} is not a triangle'.format(a,b,c))

        # PART3 - what kind of tringle is valid input
        # is a triangle equilateral
        if len(list(set([a,b,c]))) == 1:
            print '{0}, {1}, {2} - Triangle is equilateral'.format(a,b,c)

        # is a triangle isosceles
        elif len(list(set([a,b,c]))) == 2:
            print '{0}, {1}, {2} - Triangle is isosceles'.format(a,b,c)

        # is a triangle scalene
        else:
            print '{0}, {1}, {2} - Triangle is scalene'.format(a,b,c)

    @staticmethod
    def generate_random_valid_value():
        return random.randrange(1, 10)

    @staticmethod
    def generate_random_letter_value():
        return random.choice(string.letters)

    @staticmethod
    def generate_random_symbol_value():
        return random.choice(string.punctuation)

    def generate_invalid_set(self, equals=True):
        while True:
            try:
                valid_side = self.generate_random_valid_value()
                invalid_side1 = random.randrange(1, valid_side)
                break
            except ValueError:
                print 'failing running generate_invalid_set()'

        invalid_side2 = valid_side - invalid_side1
        if not equals:
            invalid_side2 = invalid_side2 -1

        return valid_side, invalid_side1, invalid_side2

    @staticmethod
    def generate_valid_scalene():
        side1 = random.randrange(2, 8)
        side2 = random.randrange(side1+1, 9)
        side3 = random.randrange(side2+1, 10)

        while side1 + side2 <= side3:
            side3 = random.randrange(side2+1, 10)

        return side1, side2, side3

    def validate_negative_value_error(self, values):
        random.shuffle(values)
        self.assertRaises(ValueError, self.triangle_app, values[0], values[1], values[2])
        print 'Successfully verified (negative) ValueError with parameters = {0}, {1}, {2}'.format(values[0], values[1], values[2])

    def validate_positive_value_error(self, values):
        self.triangle_app(values[0], values[1], values[2])
        print 'Successfully verified (positive) with triangle parameters = {0}, {1}, {2}'.format(values[0], values[1], values[2])

    def validate_negative_type_error(self, *args):
        # used to validate if triangle_app has the requisite number of arguments passed
        random.shuffle(*args)
        self.assertRaises(TypeError, self.triangle_app, *args)
        print 'Successfully verified (negative) TypeError with parameters = {0}'.format(*args)

    def validate_mixed_invalid(self, values):
        random.shuffle(values)
        letter_symbol = ''.join(values)
        self.validate_negative_value_error([self.generate_random_valid_value(), self.generate_random_valid_value(), letter_symbol])


# unittests
class TriangleTests(unittest.TestCase, Triangle):
    # just unittest functions
    def test_zero_value(self):
        self.validate_negative_value_error([self.generate_random_valid_value(), self.generate_random_valid_value(), 0])

    def test_negative_value(self):
        self.validate_negative_value_error([self.generate_random_valid_value()*-1, self.generate_random_valid_value(), self.generate_random_valid_value()])

    def test_negative_set_includes_high_boundary(self):
        self.validate_negative_value_error([self.generate_random_valid_value(), self.generate_random_valid_value(), 10])

    def test_validate_negative_letter_input(self):
        self.validate_negative_value_error([self.generate_random_valid_value(), self.generate_random_valid_value(), self.generate_random_letter_value()])

    def test_validate_negative_symbol_input(self):
        self.validate_negative_value_error([self.generate_random_valid_value(), self.generate_random_valid_value(), self.generate_random_symbol_value()])

    def test_validate_negative_symbol_and_letter_input(self):
        # e.g. one value for the triangle is '!a'
        letter_symbols = [self.generate_random_letter_value(), self.generate_random_symbol_value()]
        self.validate_mixed_invalid(letter_symbols)

    def test_validate_negative_number_and_letter_input(self):
        # e.g. one value for the triangle is '3F'
        number_letter = [str(self.generate_random_valid_value()), self.generate_random_symbol_value()]
        self.validate_mixed_invalid(number_letter)

    def test_validate_negative_number_and_symbol_input(self):
        # e.g. one value for the triangle is '9#'
        number_symbols = [str(self.generate_random_valid_value()), self.generate_random_letter_value()]
        self.validate_mixed_invalid(number_symbols)

    def test_validate_negative_type_input_low_boundary(self):
        self.validate_negative_type_error([self.generate_random_valid_value(), self.generate_random_valid_value()])

    def test_validate_negative_type_input_high_boundary(self):
        self.validate_negative_type_error([self.generate_random_valid_value(), self.generate_random_valid_value(), self.generate_random_valid_value(), self.generate_random_valid_value()])

    def test_validate_negative_set_equals(self):
        # invalid where 2 sides equal the other e.g. 2, 9, 7
        val1, val2, val3 = self.generate_invalid_set()
        self.validate_negative_value_error([val1, val2, val3])

    def test_validate_negative_set_less_than(self):
        # invalid where 2 sides less than the other e.g. 5, 2, 8
        val1, val2, val3 = self.generate_invalid_set(False)
        self.validate_negative_value_error([val1, val2, val3])

    def test_equilateral(self):
        equal_side = self.generate_random_valid_value()
        self.validate_positive_value_error([equal_side, equal_side, equal_side])

    def test_isosceles(self):
        equal_side = random.randrange(1,9)
        not_equal_side = random.randrange(equal_side+1, 10)

        # sum of 2 sides cannot be less than or equal to the 3rd
        while not_equal_side >= equal_side + equal_side:
            not_equal_side = random.randrange(equal_side+1, 10)
        self.validate_positive_value_error([equal_side, equal_side, not_equal_side])

    def test_scalene(self):
        val1, val2, val3 = self.generate_valid_scalene()
        self.validate_positive_value_error([val1, val2, val3])


if __name__ == "__main__":
    unittest.main()