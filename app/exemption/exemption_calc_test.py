from unittest.mock import patch
import io

from . import exemption_calc 
from .get_test import get_mock_exemption
from app.instruments.get_test import get_mock_instrument
from app.brokers.get_test import get_mock_broker


def mock_exemptions():
    with patch('app.exemption.get.get_exemptions') as mock_fetch_exemptions:
        mock_fetch_exemptions.return_value = [get_mock_exemption(broker_id=1, exemption_amount=500)]
        return mock_fetch_exemptions.return_value
    
def test_calculate_total_exemption():
    assert exemption_calc.calculate_total_exemption(mock_exemptions()) == 500 

def test_calculate_running_exemption():
    with patch('app.exemption.exemption_calc.get_instruments') as mock_get_instruments:
        mock_stock = get_mock_instrument(name="mock_instrument", trade_profit=100, broker_id=1)
        mock_get_instruments.return_value = [mock_stock]
        running_exemption = exemption_calc.calculate_running_exemption([get_mock_exemption(broker_id=1, exemption_amount=500)])
        assert running_exemption == 400

def test_calculate_running_exemption_per_broker():
    with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
        with patch('app.exemption.exemption_calc.get_brokers') as mock_get_brokers:
            mock_get_brokers.return_value = [get_mock_broker
                                            (id=1, 
                                            exemptions=[get_mock_exemption(broker_id=1, exemption_amount=500)], 
                                            stocks=[get_mock_instrument(name='mock_instrument_1', trade_profit=100, broker_id=1)]), 
                                            get_mock_broker
                                            (id = 2, 
                                            exemptions = [get_mock_exemption(broker_id=2, exemption_amount=100)], 
                                            stocks=[get_mock_instrument(name="mock_instrument_2", trade_profit=50, broker_id=2)])]
            exemption_calc.calculate_running_exemption_per_broker()
            printed_output = mock_stdout.getvalue().strip()
            expected_output = '''\
Broker test_broker_1 has remaining exemption 400
Broker test_broker_2 has remaining exemption 50
'''
            print(exemption_calc.calculate_running_exemption_per_broker()) 
            assert printed_output == expected_output.strip(), "Printed output doesn't match expected output."