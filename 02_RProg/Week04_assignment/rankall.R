#### 2. Find the best hospital ####

rankall <- function(outcome, num = "best") {
  ### Read outcome data
  ## Check that state and outcome are valid
  ## For each state, find the hospital of the given rank
  ## Return a data frame with the hospital names and the## (abbreviated) state 
  ## name
  hospital_df <- read.csv("outcome-of-care-measures.csv", colClasses = "character")
  
  ## Check if outcome query is valid
  if (outcome == "heart attack") {
    query.df = data.frame(
      "state" = hospital_df$State,
      "rate" = hospital_df$Hospital.30.Day.Death..Mortality..Rates.from.Heart.Attack,
      "name" = hospital_df$Hospital.Name)
  } else if (outcome == "heart failure") {
    query.df = data.frame(
      "state" = hospital_df$State,
      "rate" = hospital_df$Hospital.30.Day.Death..Mortality..Rates.from.Heart.Failure,
      "name" = hospital_df$Hospital.Name)
  } else if (outcome == "pneumonia") {
    query.df = data.frame(
      "state" = hospital_df$State,
      "rate" =  hospital_df$Hospital.30.Day.Death..Mortality..Rates.from.Pneumonia,
      "name" =  hospital_df$Hospital.Name)
  } else {
    stop("invalid outcome")
  }
  
  ## Placeholder name transfer
  full.list <- split(query.df, query.df$state)

  ## For state.df.index (sdi) in list:
  for (sdi in 1:length(full.list)) {
    
    ## Removes NAs
    ## Cleanse "not available" rates
    available_rates <- !(full.list[[sdi]]$rate == "Not Available")
    ## Splits by logical available_rates object
    full.list[[sdi]] <- full.list[[sdi]][available_rates, ]
    
    # state_rates: a table with columns
    # state: the state (same for everyone)
    # rate: mortality rate
    # name: the hospital name
    full.list[[sdi]] <- full.list[[sdi]][c(
      order(
        ## extracts rank as numeric (double)
        as.double(full.list[[sdi]]$rate),
        ## then, after ordering by rank, orders by name lexicographically
        full.list[[sdi]]$name)), ]
    full.list[[sdi]]$rank <- 1:length(full.list[[sdi]]$rate)
    # Functional table: state_rates_ordered

  }
  
  ## Separate unique states for later use
  uniq <- unique(hospital_df$State)
  
  ## DF with one line per state and corresponding rank, or NA
  rank.table <- data.frame("state" = uniq, "name" = replicate(54, NA))
  row.names(rank.table) = rank.table$state
  
  ## Per state ranking
  for (state in uniq) {
    # access with: test[["MA"]]["rank"]
    # W: print(state)
    # W: print(full.list[[state]])
    
    ## num.loop var allows to use num as a var,
    ## so it can variate if "worst" is queried without losing the original value
    num.loop <- num
    
    ## If num best -> 1
    ## If num worst -> tail
    ## If num integer num -> num
    if (num.loop == "best") {
        num.loop <- 1
    } else if (num.loop == "worst") { 
        num.loop <- length(full.list[[state]][['rank']])
    } else if (is.double(num.loop)) {
        num.loop <- num
    } else {
      stop("invalid rank")
    }
    
    ## Stores the hospital name of equivalent rank
    state.matrix <- as.data.frame(full.list[[state]])
    hosp_name <- state.matrix[state.matrix$rank == num.loop, ]$name
    #print(hosp_name)
    
    if (length(hosp_name) > 0 ) {
      rank.table[state, ]$name <- hosp_name  
    } else {
      rank.table[state, ]$name <- NA
    }
    
    
    ## reset num.loop so we can grab again the same rank in another state
    num.loop <- num
  }
  
  #full.list
  rank.table[order(rank.table$state, rank.table$name), ]

  ## Iterator over list, grabbing rank per state
  ## Must contain: translator (best -> 1, worst -> bottom of state)
}

## TESTS ##
# P = pass
# F = fail
# (P) rankall("heart failure")
# (P) rankall("heart failure", num = 3)
# (P) head(rankall("heart attack", 20), 10)
# (P) tail(rankall("pneumonia", "worst"), 3)
# (P) tail(rankall("heart failure"), 10)
# (P) test <- rankall("heart failure")

# [.. Usage ..]
# rankhospital("NY", "pneumonia", "best")
# rankhospital("MD", "heart attack", "worst")
# rankhospital("MN", "heart attack", 5000)
