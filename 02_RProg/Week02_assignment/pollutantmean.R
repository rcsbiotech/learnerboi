## Pollutant-mean

# Write a function named 'pollutantmean' that calculates the mean of a pollutant
# (sulfate or nitrate) across a specified list of monitors. The function 
# 'pollutantmean' takes three arguments: 'directory', 'pollutant', and 'id'. 
# Given a vector monitor ID numbers, 'pollutantmean' reads that monitors' 
#particulate matter data from the directory specified in the 'directory' 
# argument and returns the mean of the pollutant across all of the monitors, 
# ignoring any missing values coded as NA. A prototype of the function 
# is as follows

pollutantmean <- function(directory, pollutant, id = 1:332) {
  ## Start an empty vector
  values = vector()
  
  ## Captures every pollutant mean
  for (read in as.vector(id)) {
    
    if (read <= 9) {
      read <- paste("00", as.character(read), sep = "")
    } else if (9 < read & read <= 99) {
      read <- paste("0", as.character(read), sep = "")
    }
    
    # Reads the table
    fulldir = paste(directory, read, ".csv", sep="")
    table = read.csv(file = fulldir, header = TRUE)
    
    # Stores values for this table
    values = append(values, as.double(table[, pollutant]))
  }
  
  mean(values, na.rm = TRUE)
  #values
}


# Output should be 4.064
pollutantmean(directory = "./02_RProg/Week02_data/specdata/",
              pollutant = "sulfate",
              id = 1:10)

# Output should be 1.28~
pollutantmean(directory = "./02_RProg/Week02_data/specdata/",
              pollutant = "nitrate",
              id = 23)

## 88% is empty
#sum(is.na(table_test[,"sulfate"]))/dim(table_test)[1]



