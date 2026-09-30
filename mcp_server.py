import sys
import json
from client import PresentationSlideDeckSynthesizer

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "synthesize_deck",
                        "description": "Synthesizes multi-slide presentation decks with structured layouts and speaker notes.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "topic": {"type": "string"},
                                "source_text": {"type": "string"}
                            }
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        args = params.get("arguments", {})
        synth = PresentationSlideDeckSynthesizer()
        res = synth.synthesize_deck(args.get("topic", "Enterprise AI Adoption 2026"), args.get("source_text"))
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "content": [{"type": "text", "text": json.dumps(res, indent=2)}]
            }
        }
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    synth = PresentationSlideDeckSynthesizer()
    print(json.dumps(synth.synthesize_deck(), indent=2))

if __name__ == "__main__":
    main()
