no2api <- read.table("NO2DATA.txt", sep = ",")
no2api_undup <- no2api[!duplicated(no2api[, 1:4]), ]
colnames(no2api) <- c("loc", "no2.24h", "no2.1h", "time")
colnames(no2api_undup) <- c("loc", "no2.24h", "no2.1h", "time")
atzx_undup <- no2api_undup[no2api_undup$loc == "奥体中心", ]
average_undup <- no2api_undup[no2api_undup$loc == "None", ]
cpz_undup <- no2api_undup[no2api_undup$loc == "昌平镇", ]
dl_undup <- no2api_undup[no2api_undup$loc == "定陵", ]
ds_undup <- no2api_undup[no2api_undup$loc == "东四", ]
gc_undup <- no2api_undup[no2api_undup$loc == "古城", ]
gy_undup <- no2api_undup[no2api_undup$loc == "官园", ]
hdqwl_undup <- no2api_undup[no2api_undup$loc == "海淀区万柳", ]
hrz_undup <- no2api_undup[no2api_undup$loc == "怀柔镇", ]
nzg_undup <- no2api_undup[no2api_undup$loc == "农展馆", ]
syxc_undup <- no2api_undup[no2api_undup$loc == "顺义新城", ]
tt_undup <- no2api_undup[no2api_undup$loc == "天坛", ]
wsxg_undup <- no2api_undup[no2api_undup$loc == "万寿西宫", ]
all_data <- list(atzx_undup, average_undup, cpz_undup, dl_undup, ds_undup, 
                 gc_undup, gy_undup, hdqwl_undup, hrz_undup, nzg_undup,
                 syxc_undup, tt_undup, wsxg_undup)
period = c(as.POSIXlt("2016-12-09 23:00:00 CST"), as.POSIXlt("2016-12-11 01:00:00 CST"))

for (location in all_data){
  loc_iter <- location$loc[1]
  fileclass <- paste(loc_iter,"all", "png", sep = ".")
  png(filename = fileclass, width = 500, height = 500)
  gotplot(location, period, maintitle = loc_iter)
  dev.off()
  
}