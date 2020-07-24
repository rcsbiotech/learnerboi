#### 2. Find the best hospital ####

best <- function(state, outcome) {
  ## Read outcome data
  ## Check the validity of state and outcome
  ## Return the best in state (lowest 30day death rate)
  hospital_df <- read.csv("outcome-of-care-measures.csv", colClasses = "character")
  
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
  state_ordered <- state_rates[order(as.double(state_rates$rate), state_rates$name),]
  #lowest <- sort(state_rates$rate)[1]
  #print(lowest)
  head(state_ordered, 1)$name
  #state_rates[state_rates$rate == lowest, ]$name
  
}


# best("TX", "pneumonia")
# best("MD", "heart attack")
# best("MD", "heart failure")
# best("MS", "pneumonia")
# best("BB", "heart attack")
# best("NY", "hert attack")
# (F) - best("NY", "pneumonia")
