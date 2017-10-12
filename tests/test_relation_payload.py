from jsonschema import validate


def test_simple_relation_payload(minimal_relation_payload, relation_schema):
    """Test simple relation payload JSONSchema validation."""
    # Will rase in case of schema validation errors
    validate(minimal_relation_payload, relation_schema)
