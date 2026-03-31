from Storm import Storm
from tornado import Tornado
from blizzard import Blizzard
from hurricane import Hurricane
from storm_centre import StormCentre

# def test_remove_storm():
#     sc = StormCentre()
#     storm = Tornado("T1", 100)
#     sc.add_storm(storm)

#     stormcentre_result = sc.remove_storm("T1")
#     assert stormcentre_result == True
#     assert len(stormcentre.storm_list) == 0

# def test_add_storm():
#     sc = StormCentre()
#     storm = Tornado("T1", 100)
#     sc_result = sc.add_storm(storm)
#     assert sc_result == True
#     assert len(sc.storm_list) == 1

    
# def test_to_find_non_existent_storm():
#     sc = StormCentre()
#     sc_result =  sc.remove_storm("random_storm")
#     assert sc_result == False

# def test_to_remove_existing_storm():
#     sc = StormCentre()
#     storm = Tornado("T1", 100)
#     sc.add_storm(storm)

#     sc_result = sc.remove_storm("T1")
#     assert sc_result == True
#     assert len(sc.storm_list) == 0

# def test_add_more_than_20_storms():
#     sc = StormCentre()
#     for i in range(20):
#         sc.add_storm(Tornado(f"T{i}", 100))
        
#     result = sc.add_storm(Tornado("over 20", 100))
#     assert result == False


# def test_dupelicate_storm_name():
#     sc = StormCentre()
#     sc.add_storm(Tornado("storm", 100))
#     sc.add_storm(Tornado("storm", 100))

#     result = sc.add_storm(Tornado("storm", 100))
#     assert result == False

# def test_hurricane_cat_1():
#     h = Hurricane("H1", 74)
#     assert h.calculate_classification() == "Category one"

def test_hurricane_cat_1_boundrey():
    h = Hurricane("H2", 95)
    assert h.calculate_classification() == "Category one"


