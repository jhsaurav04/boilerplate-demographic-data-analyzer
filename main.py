from demographic_data_analyzer import calculate_demographic_data
import unittest
import test_module

# Run the analysis and print results
calculate_demographic_data()

# Run unit tests
print("\n" + "=" * 60)
print("RUNNING UNIT TESTS")
print("=" * 60)
unittest.main(module=test_module, argv=[''], verbosity=2, exit=False)