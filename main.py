import data
import helpers


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        # Add in S8
        print("function_created_for_test_set_route")
        pass  # Placeholder for future code

    def test_select_plan(self):
        # Add in S8
        print("function_created_for_test_select_plan")
        pass  # Placeholder for future code

    def test_fill_phone_number(self):
        # Add in S8
        print("function_created_for_test_fill_phone_number")
        pass  # Placeholder for future code

    def test_fill_card(self):
        # Add in S8
        print("function_created_for_test_fill_card")
        pass  # Placeholder for future code

    def test_comment_for_driver(self):
        # Add in S8
        print("function_created_for_test_comment_for_driver")
        pass  # Placeholder for future code

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print("function_created_for_test_order_blanket_and_handkerchiefs")
        pass  # Placeholder for future code

    def test_order_2_ice_creams(self):
        for i in range(2):  # Loop will iterate twice
            # Add in S8
            print("function_created_for_test_order_2_ice_creams")
            pass  # Placeholder for future code

    def test_car_search_model_appears(self):
        # Add in S8
        print("function_created_for_test_car_search_model_appears")
        pass  # Placeholder for future code
