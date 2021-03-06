import unittest
from unittest import mock
from report.report import *


class TestReport(unittest.TestCase):
    mock_response = {"data": [{"table": [
        {"ActiveCases": "336,838", "Deaths/1M pop": "33", "NewCases": "+381", "NewDeaths": "+5",
         "Tests/\n1M pop": "5,784", "TotalCases": "367,385", "TotalDeaths": "10,876", "TotalTests": "1,914,540",
         "Tot\u00a0Cases/1M pop": "1,110", "USAState": "USA Total"},
        {"ActiveCases": "113,792", "Deaths/1M pop": "243", "NewCases": "", "NewDeaths": "",
         "Tests/\n1M pop": "16,353", "TotalCases": "131,916", "TotalDeaths": "4,758", "TotalTests": "320,811",
         "Tot\u00a0Cases/1M pop": "6,724", "USAState": "New York"},
        {"ActiveCases": "39,995", "Deaths/1M pop": "113", "NewCases": "", "NewDeaths": "",
         "Tests/\n1M pop": "10,024", "TotalCases": "41,090", "TotalDeaths": "1,003", "TotalTests": "89,032",
         "Tot\u00a0Cases/1M pop": "4,626", "USAState": "New Jersey"},
        {"ActiveCases": "16,425", "Deaths/1M pop": "73", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "4,594",
         "TotalCases": "17,221", "TotalDeaths": "727", "TotalTests": "45,748", "Tot\u00a0Cases/1M pop": "1,729",
         "USAState": "Michigan"},
        {"ActiveCases": "15,057", "Deaths/1M pop": "10", "NewCases": "+323", "NewDeaths": "+5",
         "Tests/\n1M pop": "2,977", "TotalCases": "16,342", "TotalDeaths": "385", "TotalTests": "116,533",
         "Tot\u00a0Cases/1M pop": "417", "USAState": "California"},
        {"ActiveCases": "14,305", "Deaths/1M pop": "110", "NewCases": "", "NewDeaths": "",
         "Tests/\n1M pop": "14,831", "TotalCases": "14,867", "TotalDeaths": "512", "TotalTests": "69,166",
         "Tot\u00a0Cases/1M pop": "3,188", "USAState": "Louisiana"},
        {"ActiveCases": "13,567", "Deaths/1M pop": "38", "NewCases": "", "NewDeaths": "",
         "Tests/\n1M pop": "11,190", "TotalCases": "13,837", "TotalDeaths": "260", "TotalTests": "76,429",
         "Tot\u00a0Cases/1M pop": "2,026", "USAState": "Massachusetts"},
        {"ActiveCases": "13,275", "Deaths/1M pop": "12", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "6,119",
         "TotalCases": "13,629", "TotalDeaths": "254", "TotalTests": "126,048", "Tot\u00a0Cases/1M pop": "662",
         "USAState": "Florida"},
        {"ActiveCases": "12,872", "Deaths/1M pop": "14", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "6,556",
         "TotalCases": "13,127", "TotalDeaths": "179", "TotalTests": "83,854", "Tot\u00a0Cases/1M pop": "1,026",
         "USAState": "Pennsylvania"},
        {"ActiveCases": "11,905", "Deaths/1M pop": "24", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "4,909",
         "TotalCases": "12,262", "TotalDeaths": "307", "TotalTests": "62,942", "Tot\u00a0Cases/1M pop": "956",
         "USAState": "Illinois"},
        {"ActiveCases": "7,164", "Deaths/1M pop": "52", "NewCases": "+58", "NewDeaths": "",
         "Tests/\n1M pop": "12,527", "TotalCases": "8,384", "TotalDeaths": "381", "TotalTests": "91,375",
         "Tot\u00a0Cases/1M pop": "1,149", "USAState": "Washington"},
        {"ActiveCases": "7,179", "Deaths/1M pop": "5", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "3,061",
         "TotalCases": "8,088", "TotalDeaths": "151", "TotalTests": "85,357", "Tot\u00a0Cases/1M pop": "290",
         "USAState": "Texas"},
        {"ActiveCases": "7,054", "Deaths/1M pop": "22", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "3,037",
         "TotalCases": "7,314", "TotalDeaths": "229", "TotalTests": "31,274", "Tot\u00a0Cases/1M pop": "710",
         "USAState": "Georgia"},
        {"ActiveCases": "6,650", "Deaths/1M pop": "58", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "7,451",
         "TotalCases": "6,906", "TotalDeaths": "206", "TotalTests": "26,686", "Tot\u00a0Cases/1M pop": "1,928",
         "USAState": "Connecticut"},
        {"ActiveCases": "4,982", "Deaths/1M pop": "27", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "4,859",
         "TotalCases": "5,172", "TotalDeaths": "150", "TotalTests": "26,875", "Tot\u00a0Cases/1M pop": "935",
         "USAState": "Colorado"},
        {"ActiveCases": "4,791", "Deaths/1M pop": "21", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "3,946",
         "TotalCases": "4,944", "TotalDeaths": "139", "TotalTests": "26,191", "Tot\u00a0Cases/1M pop": "745",
         "USAState": "Indiana"},
        {"ActiveCases": "4,308", "Deaths/1M pop": "12", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "4,156",
         "TotalCases": "4,450", "TotalDeaths": "142", "TotalTests": "48,378", "Tot\u00a0Cases/1M pop": "382",
         "USAState": "Ohio"},
        {"ActiveCases": "3,770", "Deaths/1M pop": "15", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "4,933",
         "TotalCases": "4,045", "TotalDeaths": "91", "TotalTests": "29,617", "Tot\u00a0Cases/1M pop": "674",
         "USAState": "Maryland"},
        {"ActiveCases": "3,381", "Deaths/1M pop": "10", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "7,119",
         "TotalCases": "3,802", "TotalDeaths": "65", "TotalTests": "47,350", "Tot\u00a0Cases/1M pop": "572",
         "USAState": "Tennessee"},
        {"ActiveCases": "2,905", "Deaths/1M pop": "5", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "3,943",
         "TotalCases": "3,039", "TotalDeaths": "48", "TotalTests": "40,045", "Tot\u00a0Cases/1M pop": "299",
         "USAState": "North Carolina"},
        {"ActiveCases": "2,822", "Deaths/1M pop": "6", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "2,914",
         "TotalCases": "2,878", "TotalDeaths": "54", "TotalTests": "24,521", "Tot\u00a0Cases/1M pop": "342",
         "USAState": "Virginia"},
        {"ActiveCases": "2,658", "Deaths/1M pop": "9", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "4,462",
         "TotalCases": "2,722", "TotalDeaths": "52", "TotalTests": "27,173", "Tot\u00a0Cases/1M pop": "447",
         "USAState": "Missouri"},
        {"ActiveCases": "2,371", "Deaths/1M pop": "9", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "4,683",
         "TotalCases": "2,456", "TotalDeaths": "65", "TotalTests": "32,534", "Tot\u00a0Cases/1M pop": "354",
         "USAState": "Arizona"},
        {"ActiveCases": "2,361", "Deaths/1M pop": "13", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "5,021",
         "TotalCases": "2,440", "TotalDeaths": "77", "TotalTests": "29,014", "Tot\u00a0Cases/1M pop": "422",
         "USAState": "Wisconsin"},
        {"ActiveCases": "2,184", "Deaths/1M pop": "10", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "3,829",
         "TotalCases": "2,232", "TotalDeaths": "48", "TotalTests": "18,976", "Tot\u00a0Cases/1M pop": "450",
         "USAState": "South Carolina"},
        {"ActiveCases": "1,934", "Deaths/1M pop": "11", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "3,035",
         "TotalCases": "2,006", "TotalDeaths": "52", "TotalTests": "14,765", "Tot\u00a0Cases/1M pop": "412",
         "USAState": "Alabama"},
        {"ActiveCases": "1,871", "Deaths/1M pop": "16", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "7,101",
         "TotalCases": "1,953", "TotalDeaths": "46", "TotalTests": "20,756", "Tot\u00a0Cases/1M pop": "668",
         "USAState": "Nevada"},
        {"ActiveCases": "1,687", "Deaths/1M pop": "17", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "6,816",
         "TotalCases": "1,738", "TotalDeaths": "51", "TotalTests": "20,370", "Tot\u00a0Cases/1M pop": "582",
         "USAState": "Mississippi"},
        {"ActiveCases": "1,636", "Deaths/1M pop": "4", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "10,966",
         "TotalCases": "1,675", "TotalDeaths": "13", "TotalTests": "33,394", "Tot\u00a0Cases/1M pop": "550",
         "USAState": "Utah"},
        {"ActiveCases": "893", "Deaths/1M pop": "13", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "702",
         "TotalCases": "1,327", "TotalDeaths": "51", "TotalTests": "2,751", "Tot\u00a0Cases/1M pop": "339",
         "USAState": "Oklahoma"},
        {"ActiveCases": "1,157", "Deaths/1M pop": "8", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "6,663",
         "TotalCases": "1,170", "TotalDeaths": "13", "TotalTests": "11,246", "Tot\u00a0Cases/1M pop": "693",
         "USAState": "Idaho"},
        {"ActiveCases": "1,103", "Deaths/1M pop": "7", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "5,341",
         "TotalCases": "1,132", "TotalDeaths": "29", "TotalTests": "21,801", "Tot\u00a0Cases/1M pop": "277",
         "USAState": "Oregon"},
        {"ActiveCases": "815", "Deaths/1M pop": "35", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "10,888",
         "TotalCases": "1,097", "TotalDeaths": "24", "TotalTests": "7,453", "Tot\u00a0Cases/1M pop": "1,603",
         "USAState": "District Of Columbia"},
        {"ActiveCases": "1,045", "Deaths/1M pop": "26", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "8,027",
         "TotalCases": "1,082", "TotalDeaths": "27", "TotalTests": "8,481", "Tot\u00a0Cases/1M pop": "1,024",
         "USAState": "Rhode Island"},
        {"ActiveCases": "643", "Deaths/1M pop": "13", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "4,494",
         "TotalCases": "1,008", "TotalDeaths": "59", "TotalTests": "19,955", "Tot\u00a0Cases/1M pop": "227",
         "USAState": "Kentucky"},
        {"ActiveCases": "486", "Deaths/1M pop": "5", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "5,089",
         "TotalCases": "986", "TotalDeaths": "30", "TotalTests": "28,128", "Tot\u00a0Cases/1M pop": "178",
         "USAState": "Minnesota"},
        {"ActiveCases": "853", "Deaths/1M pop": "8", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "3,703",
         "TotalCases": "946", "TotalDeaths": "25", "TotalTests": "11,599", "Tot\u00a0Cases/1M pop": "302",
         "USAState": "Iowa"},
        {"ActiveCases": "772", "Deaths/1M pop": "5", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "4,435",
         "TotalCases": "927", "TotalDeaths": "16", "TotalTests": "13,264", "Tot\u00a0Cases/1M pop": "310",
         "USAState": "Arkansas"},
        {"ActiveCases": "820", "Deaths/1M pop": "9", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "3,123",
         "TotalCases": "845", "TotalDeaths": "25", "TotalTests": "9,084", "Tot\u00a0Cases/1M pop": "291",
         "USAState": "Kansas"},
        {"ActiveCases": "697", "Deaths/1M pop": "16", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "8,038",
         "TotalCases": "783", "TotalDeaths": "15", "TotalTests": "7,632", "Tot\u00a0Cases/1M pop": "825",
         "USAState": "Delaware"},
        {"ActiveCases": "555", "Deaths/1M pop": "7", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "6,500",
         "TotalCases": "715", "TotalDeaths": "9", "TotalTests": "8,734", "Tot\u00a0Cases/1M pop": "532",
         "USAState": "New Hampshire"},
        {"ActiveCases": "620", "Deaths/1M pop": "6", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "9,175",
         "TotalCases": "686", "TotalDeaths": "12", "TotalTests": "19,198", "Tot\u00a0Cases/1M pop": "328",
         "USAState": "New Mexico"},
        {"ActiveCases": "520", "Deaths/1M pop": "37", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "10,613",
         "TotalCases": "543", "TotalDeaths": "23", "TotalTests": "6,633", "Tot\u00a0Cases/1M pop": "869",
         "USAState": "Vermont"},
        {"ActiveCases": "331", "Deaths/1M pop": "8", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "4,910",
         "TotalCases": "499", "TotalDeaths": "10", "TotalTests": "6,544", "Tot\u00a0Cases/1M pop": "374",
         "USAState": "Maine"},
        {"ActiveCases": "404", "Deaths/1M pop": "4", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "3,614",
         "TotalCases": "412", "TotalDeaths": "8", "TotalTests": "6,883", "Tot\u00a0Cases/1M pop": "216",
         "USAState": "Nebraska"},
        {"ActiveCases": "293", "Deaths/1M pop": "4", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "9,610",
         "TotalCases": "387", "TotalDeaths": "5", "TotalTests": "13,665", "Tot\u00a0Cases/1M pop": "272",
         "USAState": "Hawaii"},
        {"ActiveCases": "341", "Deaths/1M pop": "2", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "5,435",
         "TotalCases": "345", "TotalDeaths": "4", "TotalTests": "9,940", "Tot\u00a0Cases/1M pop": "189",
         "USAState": "West Virginia"},
        {"ActiveCases": "281", "Deaths/1M pop": "6", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "6,705",
         "TotalCases": "319", "TotalDeaths": "6", "TotalTests": "6,985", "Tot\u00a0Cases/1M pop": "306",
         "USAState": "Montana"},
        {"ActiveCases": "193", "Deaths/1M pop": "5", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "6,965",
         "TotalCases": "288", "TotalDeaths": "4", "TotalTests": "6,020", "Tot\u00a0Cases/1M pop": "333",
         "USAState": "South Dakota"},
        {"ActiveCases": "148", "Deaths/1M pop": "4", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "9,589",
         "TotalCases": "225", "TotalDeaths": "3", "TotalTests": "7,213", "Tot\u00a0Cases/1M pop": "299",
         "USAState": "North Dakota"},
        {"ActiveCases": "160", "Deaths/1M pop": "", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "6,753",
         "TotalCases": "212", "TotalDeaths": "", "TotalTests": "3,929", "Tot\u00a0Cases/1M pop": "364",
         "USAState": "Wyoming"},
        {"ActiveCases": "170", "Deaths/1M pop": "8", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "8,509",
         "TotalCases": "191", "TotalDeaths": "6", "TotalTests": "6,284", "Tot\u00a0Cases/1M pop": "259",
         "USAState": "Alaska"},
        {"ActiveCases": "85", "Deaths/1M pop": "", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "",
         "TotalCases": "112", "TotalDeaths": "4", "TotalTests": "605", "Tot\u00a0Cases/1M pop": "",
         "USAState": "Guam"},
        {"ActiveCases": "7", "Deaths/1M pop": "", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "",
         "TotalCases": "8", "TotalDeaths": "1", "TotalTests": "33", "Tot\u00a0Cases/1M pop": "",
         "USAState": "Northern Mariana Islands"},
        {"ActiveCases": "488", "Deaths/1M pop": "6", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "1,462",
         "TotalCases": "513", "TotalDeaths": "21", "TotalTests": "4,951", "Tot\u00a0Cases/1M pop": "151",
         "USAState": "Puerto Rico"},
        {"ActiveCases": "8", "Deaths/1M pop": "", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "",
         "TotalCases": "43", "TotalDeaths": "1", "TotalTests": "266", "Tot\u00a0Cases/1M pop": "",
         "USAState": "United States Virgin Islands"},
        {"ActiveCases": "3", "Deaths/1M pop": "", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "",
         "TotalCases": "3", "TotalDeaths": "", "TotalTests": "3", "Tot\u00a0Cases/1M pop": "",
         "USAState": "Wuhan Repatriated"},
        {"ActiveCases": "46", "Deaths/1M pop": "", "NewCases": "", "NewDeaths": "", "Tests/\n1M pop": "",
         "TotalCases": "46", "TotalDeaths": "", "TotalTests": "46", "Tot\u00a0Cases/1M pop": "",
         "USAState": "Diamond Princess Cruise"},
        {"ActiveCases": "336,838", "Deaths/1M pop": "33", "NewCases": "+381", "NewDeaths": "+5",
         "Tests/\n1M pop": "5,784", "TotalCases": "367,385", "TotalDeaths": "10,876", "TotalTests": "1,914,540",
         "Tot\u00a0Cases/1M pop": "1,110", "USAState": "Total:"}]}]}

    texas_response = {"ActiveCases": "7,179", "Deaths/1M pop": "5", "NewCases": "", "NewDeaths": "",
                      "Tests/\n1M pop": "3,061", "TotalCases": "8,088", "TotalDeaths": "151", "TotalTests": "85,357",
                      "Tot\u00a0Cases/1M pop": "290", "USAState": "Texas"}

    def test_get_report_by_country_no_state(self):
        report = Report("")
        response = report.get_report_by_country(self.mock_response)
        expected_response = self.mock_response, 200
        self.assertEqual(response, expected_response)

    def test_get_report_by_country_with_state(self):
        report = Report("Texas")
        response = report.get_report_by_country(self.mock_response)
        expected_response = self.texas_response, 200
        self.assertEqual(response, expected_response)

    def test_get_report_by_country_bad_state(self):
        report = Report("FakeState")
        response = report.get_report_by_country(self.mock_response)
        expected_response = "Didn't find any data for state: FakeState", 404
        self.assertEqual(response, expected_response)

    def test_get_report_by_country_Unmarshalling_error(self):
        report = Report(None)
        response = report.get_report_by_country(self.mock_response)
        expected_response = "Internal Server Error: Unmarshalling error ", 500
        self.assertEqual(response, expected_response)

    @mock.patch('requests.get')
    def test_get_all_reports_happy_path(self, mock_get):
        report = Report(None)
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = self.mock_response
        response = report.get_all_reports()
        expected_response = self.mock_response
        self.assertEqual(response, expected_response)

    @mock.patch('requests.get', side_effect=Exception)
    def test_get_all_reports_sad_path(self, mock_get):
        report = Report(None)
        response = report.get_all_reports()
        expected_response = "Internal Server Error: Failure calling downstream", 500
        self.assertEqual(response, expected_response)


if __name__ == '__main__':
    unittest.main()
