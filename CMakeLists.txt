cmake_minimum_required(VERSION 3.22)

project(one CXX)

# === Required packages ===
find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
include_directories(${Python3_INCLUDE_DIRS})
link_directories(${Python3_LIBRARY_DIRS})
find_package(SWIG 4.1 REQUIRED COMPONENTS python)
include(UseSWIG)

# === buildlib target ===
add_library(one SHARED one.cpp)
target_include_directories(one PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
set_target_properties(one PROPERTIES OUTPUT_NAME "one")
add_library(buildlib ALIAS one)

# === installlib target ===
install(TARGETS one LIBRARY DESTINATION lib)
install(FILES one.h DESTINATION include)
add_custom_target(installlib DEPENDS buildlib COMMAND ${CMAKE_COMMAND} --install .)

# === wrapper target ===
set(CMAKE_SWIG_OUTDIR ${CMAKE_BINARY_DIR}/python)
set_source_files_properties(one.i PROPERTIES CPLUSPLUS ON)
swig_add_library(wrapper LANGUAGE python SOURCES one.i)
target_link_libraries(wrapper PRIVATE ${Python3_LIBRARIES} one)
target_include_directories(wrapper PRIVATE ${Python3_INCLUDE_DIRS} ${CMAKE_CURRENT_SOURCE_DIR})
set_target_properties(wrapper PROPERTIES OUTPUT_NAME "one")

# === pkg target ===
add_custom_target(pkg ALL
    COMMAND ${CMAKE_COMMAND} -E make_directory ${CMAKE_CURRENT_BINARY_DIR}/dist/one
    COMMAND ${CMAKE_COMMAND} --build . --target wrapper
    COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_CURRENT_BINARY_DIR}/python/one.py ${CMAKE_CURRENT_BINARY_DIR}/dist/one/one.py
    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:wrapper> ${CMAKE_CURRENT_BINARY_DIR}/dist/one/_one.so
    COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_CURRENT_SOURCE_DIR}/one.h ${CMAKE_CURRENT_BINARY_DIR}/dist/one/one.h
    COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_CURRENT_SOURCE_DIR}/setup.py ${CMAKE_CURRENT_BINARY_DIR}/dist/one/setup.py
    COMMENT "Generating Python package"
    DEPENDS wrapper
)
