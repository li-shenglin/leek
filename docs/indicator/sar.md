### SAR(Stop and Reverse)

SAR指标的公式是基于价格的高低点以及之前的SAR值来计算的，具体来说，SAR指标的计算公式如下：

$$
{SAR_t} = {SAR_{t-1}} + {α_{t-1}} ({EP_{t-1}} – {SAR_{t-1}})
$$

其中：

SAR = 抛物线指标

t = 交易日

α = 加速因子，0.02 ≤ α ≤ 0.2

EP = 区间极值（最高点或最低点）

在上升趋势中，如果前一天的SAR值低于前一天的最高价，区间极值（EP）就等于当前的最高价。
在下跌趋势中，如果前一天的SAR值高于前一天的最低价，区间极值（EP）就等于当前的最低价。
而加速因子（α）是一个随着时间递增而增加的值，一般情况下它的起始值为0.02，上限值为0.20。当趋势继续进行时，加速因子的值也会持续增加，加速指标也会越来越接近价格，以提供更好的止损点。
