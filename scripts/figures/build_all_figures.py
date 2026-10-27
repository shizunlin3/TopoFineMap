from pathlib import Path
import subprocess, sys
HERE=Path(__file__).resolve().parent
for name in [
    "render_main_figure3.py",
    "render_main_figure4.py",
    "render_supp_s7.py",
    "render_supp_s8.py",
    "render_supp_s9.py",
    "render_supp_s10.py",
]:
    print("RUN",name)
    subprocess.run([sys.executable,str(HERE/name)],check=True)
print("DONE")
