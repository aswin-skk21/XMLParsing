import csv
import os
import xml.etree.ElementTree as ET

def ParseXML(csv_filename):
    output_file_name = "output.csv"

    with open(output_file_name, 'w', newline='', encoding='utf-8') as output_file_handle:
        writer = csv.writer(output_file_handle)

        writer.writerow(["JobID", "Schedule Name", "Schedule Time",
                         "Schedule Type", "Enabled"])

        with open('locations.csv', 'r', newline='') as input_locations_file:
            reader = csv.reader(input_locations_file)
            for row in reader:
                xml_file_path = row[0]
                print(f"Parsing XML file: {xml_file_path}")

                tree = ET.parse(xml_file_path)
                root = tree.getroot()

                xmlList = []

                schedule_name_elem = root.find('id')
                xmlList.append(schedule_name_elem.text if schedule_name_elem is not None else "N/A")
                
                schedule_name_elem = root.find('scheduleName')
                xmlList.append(schedule_name_elem.text if schedule_name_elem is not None else "N/A")

                schedule_time_elem = root.find('scheduleTime')
                xmlList.append(schedule_time_elem.text if schedule_time_elem is not None else "N/A")

                schedule_type_elem = root.find('scheduleType')
                xmlList.append(schedule_type_elem.text if schedule_type_elem is not None else "N/A")

                enabled_elem = root.find('enabled')
                xmlList.append(enabled_elem.text if enabled_elem is not None else "N/A")

                print("Writing data to output.csv")
                writer.writerow(xmlList)

    print(f"\nAll processed XML data written to {output_file_name}")