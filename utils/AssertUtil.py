import jsonpath


class AssertUtil:

    @staticmethod
    def equals(check_value, expect_value):
        """相等"""
        assert check_value == expect_value, f'{check_value} == {expect_value}'

    @staticmethod
    def less_than(check_value, expect_value):
        """小于"""
        assert check_value < expect_value, f'{check_value} < {expect_value})'

    @staticmethod
    def less_than_or_equals(check_value, expect_value):
        """小于等于"""
        assert check_value <= expect_value, f'{check_value} <= {expect_value})'

    @staticmethod
    def greater_than(check_value, expect_value):
        """大于"""
        assert check_value > expect_value, f'{check_value} > {expect_value})'

    @staticmethod
    def greater_than_or_equals(check_value, expect_value):
        """大于等于"""
        assert check_value >= expect_value, f'{check_value} >= {expect_value})'

    @staticmethod
    def not_equals(check_value, expect_value):
        """不等于"""
        assert check_value != expect_value, f'{check_value} != {expect_value})'

    @staticmethod
    def contains(check_value, expect_value):
        """包含"""
        assert expect_value in check_value, f'{expect_value} in {check_value})'

    @staticmethod
    def startswith(check_value, expect_value):
        """以什么开头"""
        assert str(check_value).startswith(str(expect_value)), f'{str(check_value)} startswith {str(expect_value)})'

    @staticmethod
    def endswith(check_value, expect_value):
        """以什么结尾"""
        assert str(check_value).endswith(str(expect_value)), f'{str(check_value)} endswith {str(expect_value)})'

    @staticmethod
    def length(check_value, expect_value):
        """校验数量"""
        assert len(check_value) == expect_value, f'{str(check_value)} == {str(expect_value)})'

    def extract_by_jsonpath(self, extract_value: dict, extract_expression: str):  # noqa
        """
            json path 取值
        :param extract_value: response.json()
        :param extract_expression: eg: '$.code'
        :return: None或 提取的第一个值 或全部
        """
        if not isinstance(extract_expression, str):
            return extract_expression
        extract_value = jsonpath.jsonpath(extract_value, extract_expression)
        if not extract_value:
            return
        elif len(extract_value) == 1:
            return extract_value[0]
        else:
            return extract_value

    def validate_response(self, response, validate_check):
        """校验结果"""
        for check in validate_check:
            for check_type, check_value in check.items():
                # 实际结果
                actual_value = self.extract_by_jsonpath(response, check_value[0])
                # 期望结果
                expect_value = check_value[1]
                if check_type in ["eq", "equals", "equal"]:
                    self.equals(actual_value, expect_value)
                elif check_type in ["lt", "less_than"]:
                    self.less_than(actual_value, expect_value)
                elif check_type in ["le", "less_or_equals"]:
                    self.less_than_or_equals(actual_value, expect_value)
                elif check_type in ["gt", "greater_than"]:
                    self.greater_than(actual_value, expect_value)
                elif check_type in ["ne", "not_equal"]:
                    self.not_equals(actual_value, expect_value)
                elif check_type in ["contains"]:
                    self.contains(actual_value, expect_value)
                elif check_type in ["startswith"]:
                    self.startswith(actual_value, expect_value)
                elif check_type in ["endswith"]:
                    self.endswith(actual_value, expect_value)
                elif check_type in ["length"]:
                    self.length(actual_value, expect_value)
                else:
                    print(f'{check_type}  not valid check type')
