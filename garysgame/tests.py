from units import Unit


class UnitTester:
    ''' Each test focuses on a single piece of functionality, that might involve
    one method, or several methods. Each test method has different parameters,
    since each method is testing different things in the Unit class '''
    def test_type(self, unit, type, expected_output_type):
        print('\nTesting setting/getting the type property.')
        unit.type = type
        output_type = unit.type
        if expected_output_type == output_type:
            print('Test passed')
        else:
            print('Test failed:', output_type, "didn't match", expected_output_type)

    def test_unit_specific_property(self, unit, property_name, input_value, expected_output_value):
        ''' It tests one piece of functionality, setting a property, but it takes
        two methods. You can't test setting a property's value, which uses
        set_property(), without getting that property's value as well, by using
        get_property() '''
        print('\nTesting setting/getting a unit-specific property.')
        unit.set_property(property_name, input_value)
        output_value = unit.get_property(property_name)
        if expected_output_value == output_value:
            print('Test passed')
        else:
            print('Test failed:', output_value, "didn't match", expected_output_value)

    def test_change_property(self, unit, property_name, input_value, expected_output_value):
        ''' This assumes you've set the starting state correctly... otherwise, it will
        ALWAYS fail '''
        print("\nTesting changing an existing property's value.")
        unit.set_property(property_name, input_value)
        output_value = unit.get_property(property_name)
        if expected_output_value == output_value:
            print('Test passed')
        else:
            print('Test failed:', output_value, "didn't match", expected_output_value)

    def test_non_existent_property(self, unit, property_name):
        ''' This shows that we're not just dealing with happy paths... it shows Unit deals
        with uses that are outside of the norm '''
        print("\nTesting getting a non-existent property's value.")
        try:
            output_value = unit.get_property(property_name)
        except KeyError as e:
            print('Test passed')
            return
        print('Test failed.')


if __name__ == '__main__':
    tester = UnitTester()
    unit = Unit(1000)
    tester.test_type(unit, 'infantry', 'infantry')
    tester.test_unit_specific_property(unit, 'hitPoints', 25, 25)
    tester.test_change_property(unit, 'hitPoints', 15, 15)
    tester.test_non_existent_property(unit, 'strength')
