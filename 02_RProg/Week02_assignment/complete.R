## Find complete cases!

complete <- function(directory, id = 1:332) {
  ## Start an empty vector
  df <- data.frame(id = 0, nobs = 0)
  
  ## Captures every pollutant mean
  for (read in as.vector(id)) {
    
    ## Raw ID value
    raw <- read
    
    if (read <= 9) {
      read <- paste("00", as.character(read), sep = "")
    } else if (9 < read & read <= 99) {
      read <- paste("0", as.character(read), sep = "")
    }
    
    # Reads the table
    fulldir = paste(directory, read, ".csv", sep="")
    table = read.csv(file = fulldir, header = TRUE)
    
    # Gets complete cases as a logical vector,
    # parse it back as a sum of all TRUE values
    cases <- sum(complete.cases(table))
    df <- rbind(df, c(raw, cases))
    
  }
  
  # Adjust colnames for output
  #colnames(df) = c("id", "nobs")
  df[-1, ]
  
}



complete(directory = "./02_RProg/Week02_data/specdata/",
         id = 30:25)

