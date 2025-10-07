import asyncio
import logging
import os
import sys
from datetime import datetime
from typing import Dict, List

from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)

mcp = FastMCP("File-Search")

print("[DEBUG] MCP server starting...", file=sys.stderr)

ROOT_DIR = "D:/"


def search_files(
    keyword: str, base_path: str = ROOT_DIR, max_results: int = 20
) -> list[dict]:
    results = []
    for dirpath, _, filenames in os.walk(base_path):
        for fname in filenames:
            if keyword.lower() in fname.lower():
                fpath = os.path.abspath(os.path.join(dirpath, fname))
                try:
                    stat = os.stat(fpath)
                    results.append(
                        {
                            "파일명": fname,
                            "경로": fpath,
                            "크기(bytes)": stat.st_size,
                            "생성일": datetime.fromtimestamp(stat.st_ctime).strftime(
                                "%Y-%m-%d %H:%M:%S"
                            ),
                        }
                    )
                    if len(results) >= max_results:
                        return results
                except Exception as e:
                    logging.warning(f"파일 접근 오류: {fpath} - {e}")
    return results


@mcp.tool()
async def find_files(keyword: str) -> str:
    logging.info(f"{keyword} 키워드로 파일 검색 시작")
    loop = asyncio.get_event_loop()

    found = await loop.run_in_executor(None, search_files, keyword)
    if not found:
        return f"{keyword} 키워드로 파일을 찾을 수 없습니다."

    return "/n".join(
        [
            f"{r['파일명']} - {r['경로']} - {r['크기(bytes)']} - {r['생성일']}"
            for r in found
        ]
    )


if __name__ == "__main__":
    asyncio.run(mcp.run(transport="stdio"))
