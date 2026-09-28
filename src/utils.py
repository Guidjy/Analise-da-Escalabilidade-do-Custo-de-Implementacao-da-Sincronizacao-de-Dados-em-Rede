import pathlib as pl

def get_property_count(synched_properties: dict[str, list[str]]):
    total_properties_count = 0

    for properties in synched_properties.values():
        total_properties_count += len(properties)

    return total_properties_count


def get_toolitem_path(toolitem: str):
    project_base_dir = pl.Path(r'E:\simulator\ASTROS2020-Simulator-Project\Assets')
    toolitems_base_dir = project_base_dir / 'ToolItems'
    toolitem_file_paths = list(toolitems_base_dir.rglob('*.cs'))

    for file_path in toolitem_file_paths:
        if file_path.name == toolitem:
            return file_path

    print(F'{toolitem} FILE PATH NOT FOUND!')
    return None