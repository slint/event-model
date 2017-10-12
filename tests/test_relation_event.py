from jsonschema import validate


def test_simple_relation_payload(minimal_relation_event, event_schema):
    """Test simple relation event JSONSchema validation."""
    # Will rase in case of schema validation errors
    validate(minimal_relation_event, event_schema)


def test_ads_example_events(ads_example_events, event_schema):
    """Test simple relation event JSONSchema validation."""
    # Will rase in case of schema validation errors
    for ev in ads_example_events:
        validate(ev, event_schema)
