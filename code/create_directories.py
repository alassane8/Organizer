def create_directories(base_path, directories):
    for directory in directories:
        dir_path = base_path / directory
        if not dir_path.exists():
            dir_path.mkdir()
            print(f"Created directory: {dir_path}")
