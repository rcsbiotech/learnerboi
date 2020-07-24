#### 2. Find the best hospital ####

rankhospital <- function(state, outcome, num) {
  hospital_df <- read.csv("outcome-of-care-measures.csv", colClasses = "character")
  ## Read outcome data
  ## Check the validity of state and outcome
  ## Return the best in state (lowest 30day death rate)
  
  ## Check if state exists
  exists_state <- sum(grep(pattern = state, x = hospital_df$State))
  if (exists_state <= 0) { 
    stop("Invalid state")
  }
  
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
  
  ## Finds the lowest on state
  state_rates <- query.df[query.df$state == state,]
  
  ## Cleanse "not available" rates
  available_rates <- !(state_rates$rate == "Not Available")
  ## Splits by logical available_rates object
  state_rates_clean <- state_rates[available_rates, ]
  
  # state_rates: a table with columns
    # state: the state (same for everyone)
    # rate: mortality rate
    # name: the hospital name
  state_rates_ordered <- state_rates_clean[c(order(as.double(
    state_rates_clean$rate),
    state_rates_clean$name)), ]
  state_rates_ordered$rank <- 1:length(state_rates_ordered$rate)
  # Functional table: state_rates_ordered
  

  
  ## Parsing the user query "num"
    # if integer N: top N rates
    # if char "best": top 1
    # if char "worst": bottom 1 integer
  
  if (num == "best") { num <- 1 }
  if (num == "worst") { num <- length(state_rates_ordered$rank)}

  ## Prints the final result: the name corresponding to number
  return <- state_rates_ordered[state_rates_ordered$rank == num, ]$name
  
  ## If it doesn't exist..
  if (length(return) == 0) {
    print(NA)
  } else {
    print(return)
  }
  

  
}

# [.. Usage ..]
# rankhospital("NY", "pneumonia", "best")
# rankhospital("MD", "heart attack", "worst")
# rankhospital("MN", "heart attack", 5000)
