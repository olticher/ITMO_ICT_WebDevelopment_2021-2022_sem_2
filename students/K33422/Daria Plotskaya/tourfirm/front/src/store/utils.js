export const retrievePagination = (response) => {
    const {num_pages, page_number, links: {next, previous}} = response;

    return {
        next: next,
        prev: previous,
        pages: num_pages,
        page: page_number
    }
}