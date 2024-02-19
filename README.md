# File Scanner :computer:

This Python script allows you to scan a file using the VirusTotal API to check for any potential malware or viruses. :shield:

## Prerequisites :clipboard:

Before using this script, you need to have the following installed:

- Python 3 :snake:
- The `virus_total_apis` library (`pip install virus_total_apis`) :package:

## Usage :hammer_and_wrench:

1. Clone the repository or download the `virus_total.py` file. :arrow_down:
2. Open a terminal or command prompt. :computer:
3. Navigate to the directory containing the `virus_total.py` file. :file_folder:
4. Run the script with the following command:
```python virus_total.py <file_name>```

## Notes :pencil:

- Ensure that you have obtained a VirusTotal API key. Replace `<your_api_key_here>` in the script with your actual API key. :key:
- This script calculates the MD5 hash of the file and uses it to retrieve the file report from VirusTotal. :1234:
- The response from VirusTotal is printed in JSON format with proper indentation. :page_facing_up:


<img src="https://github.com/run9c/virus-scanner/blob/main/assets/scan.png">

## 👇 Full Result 
```
{
    "results": {
        "md5": "d41d8cd98f00b204e9800998ecf8427e",
        "permalink": "https://www.virustotal.com/gui/file/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855/detection/f-e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855-1708336157",
        "positives": 0,
        "resource": "d41d8cd98f00b204e9800998ecf8427e",
        "response_code": 1,
        "scan_date": "2024-02-19 09:49:17",
        "scan_id": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855-1708336157",
        "scans": {
            "ALYac": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "2.0.0.8"
            },
            "APEX": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "6.502"
            },
            "AVG": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "23.9.8494.0"
            },
            "AhnLab-V3": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "3.25.0.10459"
            },
            "Antiy-AVL": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "3.0"
            },
            "Arcabit": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "2022.0.0.18"
            },
            "Avast": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "23.9.8494.0"
            },
            "Avira": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "8.3.3.16"
            },
            "Baidu": {
                "detected": false,
                "result": null,
                "update": "20190318",
                "version": "1.0.0.2"
            },
            "BitDefender": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "7.2"
            },
            "BitDefenderTheta": {
                "detected": false,
                "result": null,
                "update": "20240202",
                "version": "7.2.37796.0"
            },
            "Bkav": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "2.0.0.1"
            },
            "CAT-QuickHeal": {
                "detected": false,
                "result": null,
                "update": "20240218",
                "version": "22.00"
            },
            "CMC": {
                "detected": false,
                "result": null,
                "update": "20240129",
                "version": "2.4.2022.1"
            },
            "ClamAV": {
                "detected": false,
                "result": null,
                "update": "20240218",
                "version": "1.3.0.0"
            },
            "Cynet": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "4.0.0.29"
            },
            "DrWeb": {
                "detected": false,
                "result": null,
                "update": "20240218",
                "version": "7.0.62.1180"
            },
            "ESET-NOD32": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "28760"
            },
            "Emsisoft": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "2022.6.0.32461"
            },
            "F-Secure": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "18.10.1547.307"
            },
            "FireEye": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "35.47.0.0"
            },
            "Fortinet": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "None"
            },
            "GData": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "A:25.37391B:27.34984"
            },
            "Google": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "1708331428"
            },
            "Ikarus": {
                "detected": false,
                "result": null,
                "update": "20240218",
                "version": "6.3.9.0"
            },
            "Jiangmin": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "16.0.100"
            },
            "K7AntiVirus": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "12.142.51111"
            },
            "K7GW": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "12.142.51111"
            },
            "Kaspersky": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "22.0.1.28"
            },
            "Kingsoft": {
                "detected": false,
                "result": null,
                "update": "20230906",
                "version": "None"
            },
            "Lionic": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "7.5"
            },
            "Malwarebytes": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "4.5.5.54"
            },
            "MaxSecure": {
                "detected": false,
                "result": null,
                "update": "20240217",
                "version": "1.0.0.1"
            },
            "McAfee": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "6.0.6.653"
            },
            "MicroWorld-eScan": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "14.0.409.0"
            },
            "Microsoft": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "1.1.24010.10"
            },
            "NANO-Antivirus": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "1.0.146.25796"
            },
            "Paloalto": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "0.9.0.1003"
            },
            "Panda": {
                "detected": false,
                "result": null,
                "update": "20240218",
                "version": "4.6.4.2"
            },
            "Rising": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "25.0.0.27"
            },
            "SUPERAntiSpyware": {
                "detected": false,
                "result": null,
                "update": "20240218",
                "version": "5.6.0.1032"
            },
            "Sangfor": {
                "detected": false,
                "result": null,
                "update": "20240129",
                "version": "2.23.0.0"
            },
            "Skyhigh": {
                "detected": false,
                "result": null,
                "update": "20240218",
                "version": "v2021.2.0+4045"
            },
            "Sophos": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "2.4.3.0"
            },
            "Symantec": {
                "detected": false,
                "result": null,
                "update": "20240218",
                "version": "1.21.0.0"
            },
            "TACHYON": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "2024-02-19.02"
            },
            "Tencent": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "1.0.0.1"
            },
            "TrendMicro": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "11.0.0.1006"
            },
            "TrendMicro-HouseCall": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "10.0.0.1040"
            },
            "VBA32": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "5.0.0"
            },
            "VIPRE": {
                "detected": false,
                "result": null,
                "update": "20240218",
                "version": "6.0.0.35"
            },
            "Varist": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "6.5.1.2"
            },
            "ViRobot": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "2014.3.20.0"
            },
            "VirIT": {
                "detected": false,
                "result": null,
                "update": "20240216",
                "version": "9.5.642"
            },
            "Xcitium": {
                "detected": false,
                "result": null,
                "update": "20240218",
                "version": "36449"
            },
            "Yandex": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "5.5.2.24"
            },
            "Zillya": {
                "detected": false,
                "result": null,
                "update": "20240216",
                "version": "2.0.0.5053"
            },
            "ZoneAlarm": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "1.0"
            },
            "Zoner": {
                "detected": false,
                "result": null,
                "update": "20240219",
                "version": "2.2.2.0"
            }
        },
        "sha1": "da39a3ee5e6b4b0d3255bfef95601890afd80709",
        "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        "total": 59,
        "verbose_msg": "Scan finished, information embedded"
    },
    "response_code": 200
}
```
