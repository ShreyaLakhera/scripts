getSet = function(a1) {
  a2 = c();
  for (x in 1:length(a1)) {
    if (!a1[x] %in% a2) {
      a2 = c(a2,a1[x])
    }
    }
  return(a2);
}