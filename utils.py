import os
from euxfel_bunch_pattern import PPL_BITS

def set_cpp_header():
    cpp_file = "ppl_bits.hh"
    krb_path = os.environ["KARABO"]
    cpp_file = f"{krb_path}/var/data/{cpp_file}"

    with open(cpp_file, "w") as f:

        text = (
            "const std::vector<std::pair<std::string,unsigned long>> PplBits;\n")
        for k, v in PPL_BITS.__members__.items():
            text += (f"PplBits['{k}'] = {v};\n")

        f.write(text)
