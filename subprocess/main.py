import subprocess
#path to jupyter package in your envs
path_to_jupyter="C:/Users/Admin/miniconda3/envs/spyders/Scripts/jupyter.exe"

# Kích hoạt đưa thư viện ảo vào kernel
def install_ipykernel(env, display_name):
    try:
        command = f"python -m ipykernel install --user --name {env} --display-name \"{display_name}\""
        subprocess.run(command, shell=True, check=True)
        print(f"Installed IPython kernel '{display_name}' successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing IPython kernel: {e}")

# Chạy file ipynb trong kernel
def run_ipynb(notebook_path,path_to_jupyter=path_to_jupyter):
    try:
        # Sử dụng Popen để chạy lệnh activate trong môi trường Conda
        activate_command = "conda activate spyders && "
        nbconvert_command = f"{path_to_jupyter} nbconvert --execute --inplace {notebook_path}"
        subprocess.Popen(activate_command + nbconvert_command, shell=True)
    except Exception as e:
        print(f"Lỗi khi thực thi tệp {notebook_path}: {e}")

# Sử dụng hàm để chạy tệp notebook IPython
install_ipykernel('spyders','test')
run_ipynb("test1.ipynb")
