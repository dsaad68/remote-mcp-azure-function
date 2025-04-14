import json
from dataclasses import dataclass


@dataclass
class ToolProperty:
    property_name: str
    property_type: str
    description: str

    def to_dict(self):
        return {
            "propertyName": self.property_name,
            "propertyType": self.property_type,
            "description": self.description,
        }


@dataclass
class Tool:
    name: str
    description: str
    tool_properties: list[ToolProperty]

    def tool_properties_as_json(self):
        return json.dumps([prop.to_dict() for prop in self.tool_properties])