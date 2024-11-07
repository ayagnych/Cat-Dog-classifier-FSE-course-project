#include <opencv2/opencv.hpp>
#include <iostream>
#include <filesystem>

namespace fs = std::filesystem;

int main() {
    std::string input_dir = "./input_raw";
    std::string output_dir = "./input";

    // Check if output directory exists, create it if it doesn't
    if (!fs::exists(output_dir)) {
        fs::create_directory(output_dir);
    }

    // Loop over each image in the input directory
    for (const auto &entry : fs::directory_iterator(input_dir)) {
        std::string img_path = entry.path().string();
        
        // Load the image
        cv::Mat image = cv::imread(img_path);
        if (image.empty()) {
            std::cerr << "Error: Could not load image " << img_path << std::endl;
            continue;
        }
        
        // Resize the image
        cv::Mat resized_image;
        cv::resize(image, resized_image, cv::Size(128, 128));

        // Save the resized image to the output directory
        std::string output_path = output_dir + "/" + entry.path().filename().string();
        cv::imwrite(output_path, resized_image);

        std::cout << "Processed and saved: " << output_path << std::endl;
    }

    std::cout << "Preprocessing completed." << std::endl;
    return 0;
}
