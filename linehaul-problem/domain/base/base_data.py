from abc import ABC
from datetime import datetime as DateTime, date as Date
from types import MappingProxyType
from typing import Any,Self,get_type_hints

from dataclasses import dataclass, fields

@dataclass(frozen=True)
class BaseData(ABC):

    @classmethod
    def get_csv_headers(cls) -> list[str]:
        """CSVのヘッダー一覧を取得。key未指定時はフィールド名を使用"""
        return [f.metadata.get('key', f.name) for f in fields(cls)]

    @classmethod
    def mapping_by_key(cls,row:dict[str,Any]) ->Self:
        init_args = {}
        for f in fields(cls):
            key = f.metadata.get('key', f.name)
            init_args[f.name] =row.get(key)
        return cls(**init_args)


    @classmethod
    def mapping(cls, row: dict[str,str])->Self:
        init_args = {}
        # 型ヒントを取得（Stringで定義されている場合も考慮）
        type_hints = get_type_hints(cls)

        for f in fields(cls):
            csv_key = f.metadata.get('key', f.name)
            raw_val = row.get(csv_key)

            # 値が空（Noneや空文字）の場合のハンドリング
            if raw_val is None or raw_val.strip() == "":
                init_args[f.name] = None
                continue

            # 型アノテーションに基づいたキャスト
            field_type = type_hints.get(f.name)
            init_args[f.name] = cls._cast_value(raw_val.strip(), field_type, f.metadata)

        return cls(**init_args)

    @classmethod
    def _cast_value(cls, val: str, target_type: Any, metadata: MappingProxyType[Any, Any]) -> Any:
        """文字列をアノテーションされた型に変換する"""
        try:
            # 1. 日付型 (metadataのformatを使用)
            if target_type in (DateTime, Date):
                fmt = metadata.get('format', '%Y-%m-%d')
                dt = DateTime.strptime(val, fmt)
                return dt if target_type is DateTime else dt.date()

            # 2. 数値型
            if target_type is int:
                return int(float(val))  # "1.0" のような文字列対策
            if target_type is float:
                return float(val)

            # 3. ブール型
            if target_type is bool:
                return val.lower() in ('true', '1', 'yes', 't')

            # 4. デフォルト（そのまま返す、またはstr等）
            return target_type(val)
        except (ValueError, TypeError):
            return val