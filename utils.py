import os
from euxfel_bunch_pattern import PPL_BITS

def set_cpp_header():
    cpp_file = "ppl_bits.hh"
    krb_path = os.environ["KARABO"]
    cpp_file_dir = f"{krb_path}/extern/include/ppl_bits"
    if not os.path.exists(cpp_file_dir):
        os.makedirs(cpp_file_dir)
    cpp_file = f"{cpp_file_dir}/{cpp_file}"

    with open(cpp_file, "w") as f:
        text = "#include <karabo/karabo.hpp>\n\n"
        text += (
            "const std::vector<std::pair<std::string,unsigned long>> PplBits {\n")
        ap_sign = "\""
        curll = "{"
        curlr = "}"
        for k, v in PPL_BITS.__members__.items():
            text += (f"    {curll}{ap_sign}{k}{ap_sign}, {v}{curlr},\n")
        text += "};"
        f.write(text)
