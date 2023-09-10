from data.processed.companies import get_abs_path
import great_expectations as gx

ge = gx.get_context()
df = ge.sources.pandas_default.read_csv(get_abs_path('/companies.csv'))


def main():
    # Expect columns presence
    df.expect_table_columns_to_match_ordered_list(column_list=["company_id", "logo", "name"])

    # Expect columns properties
    df.expect_column_values_to_be_unique(column="company_id")

    # Company ID is integer
    df.expect_column_values_to_be_of_type(column="company_id", type_="int")

    # Logo url and company name are a string
    df.expect_column_values_to_be_of_type(column="logo", type_="str")
    df.expect_column_values_to_be_of_type(column="name", type_="str")

    # Logo url is a valid URL
    df.expect_column_values_to_match_regex(column="logo",
                                           regex="^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$")

    # Expectation suite
    expectation_suite = df.get_expectation_suite(discard_failed_expectations=False)
    results = df.validate(expectation_suite=expectation_suite, only_return_failures=True)
    assert results['success'] is True


if __name__ == '__main__':
    main()
