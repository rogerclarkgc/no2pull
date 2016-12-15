gotplot <- function(table,  period, maintitle){
  tablec <- table
  tablec$time <- as.character(tablec$time)
  tablec$time_pox <- as.POSIXlt(tablec$time, format = "%Y-%m-%dT%H:%M:%S")
  rownames(tablec) = c(1:nrow(tablec))
  tablec <- tablec[tablec$time_pox > period[1], ]
  tablec <- tablec[tablec$time_pox < period[2], ]
  plot(tablec[tablec$no2.1h!=0, ]$time_pox, tablec[tablec$no2.1h!=0, ]$no2.1h, main = maintitle, type = "b", 
       xlab = "Time", ylab = "No2 concentration/microgram/L",
       pch = 15, lwd = 1.5, col = "blue")
  abline(h = 100, col = "red", lty = 2)
}