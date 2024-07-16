from dataclasses import dataclass, fields
from datetime import datetime
import typing as tp

BASE_URL = 'https://cat-fact.herokuapp.com'


def convert_dict_to_dataclass(dataclass_type: tp.Type[dataclass], arg_dict: dict) -> tp.Any:
    fields_set = {f.name for f in fields(dataclass_type) if f.init}
    return dataclass_type(**{k: v for k, v in arg_dict.items() if k in fields_set})


@dataclass
class CatFact:
    _id: str
    text: str
    updatedAt: str | datetime
    deleted: bool
    type: str

    def __post_init__(self):
        self.updatedAt = datetime.fromisoformat(self.updatedAt.replace("Z", "+00:00"))

    def __eq__(self, other: "CatFact"):
        for field in ['_id', 'type', 'text']:
            if getattr(self, field) != getattr(other, field):
                return False
        return True

    def __hash__(self):
        return hash(self._id)

    def __repr__(self):
        return self._id

