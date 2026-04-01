from pathlib import Path

class PathSetting:

    def __init__(self, root:str, case_name:str):
        self.root: Path =Path(root)
        if not self.root.exists():
            raise NotImplementedError(f"{root}はありません。")
        self.case_name:str =case_name

    @property
    def case_root(self)->Path:
        return self.root /"case"

    @property
    def case(self) ->Path:
        return self.case_root / self.case_name

    @property
    def network(self)->Path:
        return self.case / "network.json"

    @property
    def order(self)->Path:
        return self.case / "order.csv"

    @property
    def routing_table(self)->Path:
        return self.case / "routing_table.json"