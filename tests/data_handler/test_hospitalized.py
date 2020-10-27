from collections import defaultdict

from covid19_il.tests.data_handler.data_handler_tests_utils import DataHandlerTestsUtils
from covid19_il.data_handler.data_handlers.hospitalized import Hospitalized
from covid19_il.data_handler.enums.resource_id import ResourceId


class TestHospitalized(DataHandlerTestsUtils):
    """ Tests for Deaths Data Handler Class.

    Methods:
        setUp(self): Announce of starting the class's tests, initialize & verify cities data handler's instance.
        test_hospitalized_total_stats(self): Tests results data & type of hospitalized total stats.
        test_hospitalized_stats_by_date(self): Tests results data & type of hospitalized stats by date.

    """

    def setUp(self) -> None:
        """ Announce of starting the class's tests, initialize & verify deaths data handler's instance """
        print("testing Deaths Class...")
        self.data_handler_1 = self._init_mocked_data_handler(json_file_path="json_files/hospitalized_mocked_data.json",
                                                             resource_id_enum=ResourceId.HOSPITALIZED_DATA_RESOURCE_ID)
        self._check_base_step_of_all_methods(data_handler=self.data_handler_1, class_type=Hospitalized)

    def test_hospitalized_total_stats(self) -> None:
        """ Tests results data & type of hospitalized total stats  """
        # Get Data
        data = self.data_handler_1.hospitalized_total_stats()
        results = defaultdict(None,
                              {'2020-03-11': {'מאושפזים': 79, 'אחוז נשים מאושפזות': 36.7, 'גיל ממוצע מאושפזים': 48, 'סטיית תקן גיל מאושפזים': 17.9, 'מונשמים': '<15', 'אחוז נשים מונשמות': 20.0, 'גיל ממוצע מונשמים': 64, 'סטיית תקן גיל מונשמים': 15.4, 'חולים קל': 72, 'אחוז נשים חולות קל': 37.5, 'גיל ממוצע חולים קל': 47, 'סטיית תקן גיל חולים קל': 17.3, 'חולים בינוני': 'NULL', 'אחוז נשים חולות בינוני': 'NULL', 'גיל ממוצע חולים בינוני': 'NULL', 'סטיית תקן גיל חולים בינוני': 'NULL', 'חולים קשה': '<15', 'אחוז נשים חולות קשה': 33.3, 'גיל ממוצע חולים קשה': 67, 'סטיית תקן גיל חולים קשה': 16.3, 'חולים קשה מצטבר': '<15'},
                               '2020-03-12': {'מאושפזים': 101, 'אחוז נשים מאושפזות': 39.6, 'גיל ממוצע מאושפזים': 50, 'סטיית תקן גיל מאושפזים': 18.1, 'מונשמים': '<15', 'אחוז נשים מונשמות': 20.0, 'גיל ממוצע מונשמים': 64, 'סטיית תקן גיל מונשמים': 15.4, 'חולים קל': 94, 'אחוז נשים חולות קל': 40.4, 'גיל ממוצע חולים קל': 49, 'סטיית תקן גיל חולים קל': 17.8, 'חולים בינוני': 'NULL', 'אחוז נשים חולות בינוני': 'NULL', 'גיל ממוצע חולים בינוני': 'NULL', 'סטיית תקן גיל חולים בינוני': 'NULL', 'חולים קשה': '<15', 'אחוז נשים חולות קשה': 33.3, 'גיל ממוצע חולים קשה': 67, 'סטיית תקן גיל חולים קשה': 16.3, 'חולים קשה מצטבר': '<15'},
                               '2020-03-13': {'מאושפזים': 119, 'אחוז נשים מאושפזות': 38.7, 'גיל ממוצע מאושפזים': 49, 'סטיית תקן גיל מאושפזים': 18.2, 'מונשמים': '<15', 'אחוז נשים מונשמות': 20.0, 'גיל ממוצע מונשמים': 64, 'סטיית תקן גיל מונשמים': 15.4, 'חולים קל': 108, 'אחוז נשים חולות קל': 38.9, 'גיל ממוצע חולים קל': 48, 'סטיית תקן גיל חולים קל': 17.5, 'חולים בינוני': '<15', 'אחוז נשים חולות בינוני': '40.0', 'גיל ממוצע חולים בינוני': '68.0', 'סטיית תקן גיל חולים בינוני': '17.0', 'חולים קשה': '<15', 'אחוז נשים חולות קשה': 33.3, 'גיל ממוצע חולים קשה': 67, 'סטיית תקן גיל חולים קשה': 16.3, 'חולים קשה מצטבר': '<15'},
                               '2020-03-14': {'מאושפזים': 157, 'אחוז נשים מאושפזות': 40.8, 'גיל ממוצע מאושפזים': 48, 'סטיית תקן גיל מאושפזים': 18.4, 'מונשמים': '<15', 'אחוז נשים מונשמות': 0.0, 'גיל ממוצע מונשמים': 70, 'סטיית תקן גיל מונשמים': 7.4, 'חולים קל': 147, 'אחוז נשים חולות קל': 41.5, 'גיל ממוצע חולים קל': 46, 'סטיית תקן גיל חולים קל': 17.5, 'חולים בינוני': '<15', 'אחוז נשים חולות בינוני': '40.0', 'גיל ממוצע חולים בינוני': '68.0', 'סטיית תקן גיל חולים בינוני': '17.0', 'חולים קשה': '<15', 'אחוז נשים חולות קשה': 20.0, 'גיל ממוצע חולים קשה': 76, 'סטיית תקן גיל חולים קשה': 10.3, 'חולים קשה מצטבר': '<15'},
                               '2020-03-15': {'מאושפזים': 196, 'אחוז נשים מאושפזות': 43.9, 'גיל ממוצע מאושפזים': 47, 'סטיית תקן גיל מאושפזים': 18.7, 'מונשמים': '<15', 'אחוז נשים מונשמות': 20.0, 'גיל ממוצע מונשמים': 74, 'סטיית תקן גיל מונשמים': 7.6, 'חולים קל': 181, 'אחוז נשים חולות קל': 44.2, 'גיל ממוצע חולים קל': 45, 'סטיית תקן גיל חולים קל': 17.6, 'חולים בינוני': '<15', 'אחוז נשים חולות בינוני': '42.9', 'גיל ממוצע חולים בינוני': '62.0', 'סטיית תקן גיל חולים בינוני': '16.4', 'חולים קשה': '<15', 'אחוז נשים חולות קשה': 37.5, 'גיל ממוצע חולים קשה': 79, 'סטיית תקן גיל חולים קשה': 9.1, 'חולים קשה מצטבר': '<15'},
                               '2020-03-16': {'מאושפזים': 216, 'אחוז נשים מאושפזות': 43.5, 'גיל ממוצע מאושפזים': 47, 'סטיית תקן גיל מאושפזים': 18.8, 'מונשמים': '<15', 'אחוז נשים מונשמות': 16.7, 'גיל ממוצע מונשמים': 74, 'סטיית תקן גיל מונשמים': 7.1, 'חולים קל': 200, 'אחוז נשים חולות קל': 44.0, 'גיל ממוצע חולים קל': 45, 'סטיית תקן גיל חולים קל': 17.8, 'חולים בינוני': '<15', 'אחוז נשים חולות בינוני': '50.0', 'גיל ממוצע חולים בינוני': '59.0', 'סטיית תקן גיל חולים בינוני': '16.1', 'חולים קשה': '<15', 'אחוז נשים חולות קשה': 30.0, 'גיל ממוצע חולים קשה': 78, 'סטיית תקן גיל חולים קשה': 8.6, 'חולים קשה מצטבר': '<15'},
                               '2020-03-17': {'מאושפזים': 248, 'אחוז נשים מאושפזות': 44.0, 'גיל ממוצע מאושפזים': 47, 'סטיית תקן גיל מאושפזים': 19.2, 'מונשמים': '<15', 'אחוז נשים מונשמות': 16.7, 'גיל ממוצע מונשמים': 74, 'סטיית תקן גיל מונשמים': 7.1, 'חולים קל': 230, 'אחוז נשים חולות קל': 44.8, 'גיל ממוצע חולים קל': 46, 'סטיית תקן גיל חולים קל': 18.5, 'חולים בינוני': '<15', 'אחוז נשים חולות בינוני': '42.9', 'גיל ממוצע חולים בינוני': '56.0', 'סטיית תקן גיל חולים בינוני': '16.6', 'חולים קשה': '<15', 'אחוז נשים חולות קשה': 27.3, 'גיל ממוצע חולים קשה': 77, 'סטיית תקן גיל חולים קשה': 8.8, 'חולים קשה מצטבר': '<15'},
                               '2020-03-18': {'מאושפזים': 295, 'אחוז נשים מאושפזות': 42.4, 'גיל ממוצע מאושפזים': 47, 'סטיית תקן גיל מאושפזים': 19.1, 'מונשמים': '<15', 'אחוז נשים מונשמות': 16.7, 'גיל ממוצע מונשמים': 74, 'סטיית תקן גיל מונשמים': 7.1, 'חולים קל': 270, 'אחוז נשים חולות קל': 43.7, 'גיל ממוצע חולים קל': 45, 'סטיית תקן גיל חולים קל': 18.3, 'חולים בינוני': '<15', 'אחוז נשים חולות בינוני': '25.0', 'גיל ממוצע חולים בינוני': '59.0', 'סטיית תקן גיל חולים בינוני': '14.8', 'חולים קשה': '<15', 'אחוז נשים חולות קשה': 30.8, 'גיל ממוצע חולים קשה': 76, 'סטיית תקן גיל חולים קשה': 9.3, 'חולים קשה מצטבר': '15.0'},
                               '2020-03-19': {'מאושפזים': 283, 'אחוז נשים מאושפזות': 41.3, 'גיל ממוצע מאושפזים': 48, 'סטיית תקן גיל מאושפזים': 19.6, 'מונשמים': '<15', 'אחוז נשים מונשמות': 36.4, 'גיל ממוצע מונשמים': 70, 'סטיית תקן גיל מונשמים': 12.8, 'חולים קל': 253, 'אחוז נשים חולות קל': 42.3, 'גיל ממוצע חולים קל': 46, 'סטיית תקן גיל חולים קל': 18.8, 'חולים בינוני': '<15', 'אחוז נשים חולות בינוני': '25.0', 'גיל ממוצע חולים בינוני': '60.0', 'סטיית תקן גיל חולים בינוני': '13.7', 'חולים קשה': '18.0', 'אחוז נשים חולות קשה': 38.9, 'גיל ממוצע חולים קשה': 73, 'סטיית תקן גיל חולים קשה': 12.4, 'חולים קשה מצטבר': '20.0'},
                               '2020-03-20': {'מאושפזים': 277, 'אחוז נשים מאושפזות': 42.2, 'גיל ממוצע מאושפזים': 50, 'סטיית תקן גיל מאושפזים': 19.3, 'מונשמים': '<15', 'אחוז נשים מונשמות': 36.4, 'גיל ממוצע מונשמים': 70, 'סטיית תקן גיל מונשמים': 12.8, 'חולים קל': 242, 'אחוז נשים חולות קל': 43.4, 'גיל ממוצע חולים קל': 48, 'סטיית תקן גיל חולים קל': 19.0, 'חולים בינוני': '15.0', 'אחוז נשים חולות בינוני': '26.7', 'גיל ממוצע חולים בינוני': '59.0', 'סטיית תקן גיל חולים בינוני': '12.5', 'חולים קשה': '20.0', 'אחוז נשים חולות קשה': 40.0, 'גיל ממוצע חולים קשה': 71, 'סטיית תקן גיל חולים קשה': 11.9, 'חולים קשה מצטבר': '23.0'}})
        # Data Validation
        self._test_two_level_depth_nested_dictionaries(data, results)

    def test_hospitalized_stats_by_date(self) -> None:
        """ Tests results data & type of hospitalized stats by date """
        # Check if raise exception occurs
        with self.assertRaises(ValueError):
            _ = self.data_handler_1.hospitalized_stats_by_date("2020-13-20")
        with self.assertRaises(ValueError):
            _ = self.data_handler_1.hospitalized_stats_by_date("2020-11-201")
        # Get Data
        data = self.data_handler_1.hospitalized_stats_by_date("2020-03-20")
        results = {'מאושפזים': 277, 'אחוז נשים מאושפזות': 42.2, 'גיל ממוצע מאושפזים': 50, 'סטיית תקן גיל מאושפזים': 19.3, 'מונשמים': '<15', 'אחוז נשים מונשמות': 36.4, 'גיל ממוצע מונשמים': 70, 'סטיית תקן גיל מונשמים': 12.8, 'חולים קל': 242, 'אחוז נשים חולות קל': 43.4, 'גיל ממוצע חולים קל': 48, 'סטיית תקן גיל חולים קל': 19.0, 'חולים בינוני': '15.0', 'אחוז נשים חולות בינוני': '26.7', 'גיל ממוצע חולים בינוני': '59.0', 'סטיית תקן גיל חולים בינוני': '12.5', 'חולים קשה': '20.0', 'אחוז נשים חולות קשה': 40.0, 'גיל ממוצע חולים קשה': 71, 'סטיית תקן גיל חולים קשה': 11.9, 'חולים קשה מצטבר': '23.0'}
        # Data Validation
        self.assertIsInstance(data, dict)
        self.assertDictEqual(data, results)
        for key, value in data.items():
            self.assertIsInstance(key, str)
            self.assertIsInstance(value, (int, float, str))
