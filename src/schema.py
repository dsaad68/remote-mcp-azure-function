"""Schema definitions for tools and their properties.

This module provides dataclasses for representing tools and their properties,
along with methods for serialization.
"""

import json
from dataclasses import dataclass


@dataclass
class ToolProperty:
    """Represents a property of a tool (argument).

    Attributes:
        property_name (str): The name of the property.
        property_type (str): The data type of the property.
        description (str): Description of what the property does.
    """

    property_name: str
    property_type: str
    description: str

    def to_dict(self) -> dict:
        """Convert the property to a dictionary representation.

        Returns:
            dict: Dictionary containing the property's attributes.
        """
        return {
            "propertyName": self.property_name,
            "propertyType": self.property_type,
            "description": self.description,
        }


@dataclass
class Tool:
    """Represents a tool with its properties.

    Attributes:
        name (str): The name of the tool.
        description (str): Description of what the tool does.
        tool_properties (list[ToolProperty]): List of properties for this tool.
    """

    name: str
    description: str
    tool_properties: list[ToolProperty]

    def tool_properties_as_json(self) -> str:
        """Convert the tool's properties to a JSON string.

        Returns:
            str: JSON string representing the tool's properties.
        """
        return json.dumps([prop.to_dict() for prop in self.tool_properties])