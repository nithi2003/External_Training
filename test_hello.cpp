#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include "hello_world.cpp"  // Include the file with the main program

TEST_CASE("Test Hello World Output", "[hello]") {
    // Redirect stdout to a stringstream to capture the output
    std::stringstream buffer;
    std::streambuf* old_stdout = std::cout.rdbuf(buffer.rdbuf());

    // Call the main function from the hello_world.cpp program
    main();

    // Restore the original stdout
    std::cout.rdbuf(old_stdout);

    // Check if the output matches "Hello, World!\n"
    REQUIRE(buffer.str() == "Hello, World!\n");
}
