#include <iostream>
#include <fstream>
#include <filesystem>
#include <string>
#include <sstream>

namespace fs = std::filesystem;

void postprocess(const std::string& input_dir, const std::string& output_dir) {
    // Ensure the output directory exists
    fs::create_directory(output_dir);

    for (const auto& entry : fs::directory_iterator(input_dir)) {
        std::ifstream infile(entry.path());
        std::string line;

        if (std::getline(infile, line)) {
            std::istringstream iss(line);
            std::string filename;
            std::string prediction;
            std::string first_part, second_part;

            // Parse line format: "filename [[x y]]"
            if (iss >> filename >> first_part >> second_part) {
                // Remove brackets from the prediction parts
                first_part.erase(0, 2);  // Remove "[["
                second_part.erase(second_part.size() - 2);  // Remove "]]"

                // Determine label based on parsed prediction
                std::string label;
                if (first_part == "1." && second_part == "0.") {
                    label = "Cat";
                } else if (first_part == "0." && second_part == "1.") {
                    label = "Dog";
                } else {
                    label = "Unknown";  // Handle unexpected cases
                }

                // Save the label in the output directory
                std::string output_path = output_dir + "/" + filename + "_label.txt";
                std::ofstream outfile(output_path);
                outfile << filename << " --> " << label << std::endl;
                //std::cout << filename << " --> " << label << std::endl;
            }
        }
    }
}

int main() {
    std::string input_dir = "./output_raw";
    std::string output_dir = "./output";
    postprocess(input_dir, output_dir);

    // Print all files in the output directory
    for (const auto& entry : fs::directory_iterator(output_dir)) {
        std::ifstream infile(entry.path());
        std::string line;
        while (std::getline(infile, line)) {
            std::cout << line << std::endl;
        }
    }
    std::cout << "Postprocessing completed." << std::endl;
    return 0;
}
