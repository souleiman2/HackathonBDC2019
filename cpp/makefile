# Variables
SRC_DIR := src
BIN_DIR := bin

LIB_DIR := lib
INC_DIR := include


SRC := $(wildcard $(SRC_DIR)/*.cpp)
OBJ := $(addprefix $(BIN_DIR)/, $(notdir $(SRC:.cpp=.o)))


TRG = SqlTest.exe

LIBS = 

# Phony
.PHONY: all clean

all: $(TRG)

clean:
	rm -f $(BIN_DIR)/* $(TRG)


# Flags
CFLAGS = -I $(INC_DIR) -g -Wall -O0 -std=c++11

CXXFLAGS =

LDFLAGS = -L $(LIB_DIR) $(LIBS)



# Rules
$(TRG): $(OBJ)
	$(CXX) $(LDFLAGS) -o $@ $^
	
	
$(BIN_DIR)/%.o: $(SRC_DIR)/%.cpp | $(BIN_DIR)
	$(CXX) $(CFLAGS) $(CXXFLAGS) -o $@ -c $<
	
$(BIN_DIR):
	mkdir $@