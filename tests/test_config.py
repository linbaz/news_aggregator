import importlib.util
from tools import gen_config

def test_config_generated(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    (tmp_path.parent / "student_id.txt").write_text("TestStudent", encoding="utf-8")

    gen_config.generate_config()

    import importlib.util
    config_path = tmp_path.parent / "config.py"
    spec = importlib.util.spec_from_file_location("config", str(config_path))
    cfg = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cfg)

    assert cfg.STUDENT_ID.startswith("TestStudent_")
    assert isinstance(cfg.SOURCES, list) and cfg.SOURCES == []