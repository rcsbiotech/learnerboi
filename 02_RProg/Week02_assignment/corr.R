## Correlates pollution!

corr <- function(directory, threshold = 0) {

  ## Starts output vector
  out.corr <- vector()
  
  ## Captures every pollutant values
  for (read in 1:332) {
    
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
    #print(cases)
    
    table <- table[complete.cases(table), ]
    
    if (cases > threshold) {
      #print(cor(x <- table$sulfate, y <- table$nitrate))
      out.corr <- append(out.corr, cor(x <- table$sulfate, y <- table$nitrate))
    }
    
    
  }
  out.corr

}

