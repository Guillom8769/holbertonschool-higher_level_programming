#!/usr/bin/python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The filename to save the XML data to.
    """
    # Create the root element
    root = ET.Element('data')

    # Iterate through dictionary items and add them as child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Write the XML tree to the specified file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file into a Python dictionary.

    Args:
        filename (str): The filename of the XML file to read from.

    Returns:
        dict: The deserialized dictionary.
    """
    # Parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Reconstruct the dictionary
    result = {}
    for child in root:
        result[child.tag] = child.text

    return result
