import { Injectable, NotFoundException } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';
import { CreateBlogPostDto } from './dto/create-blog-post.dto';
import { UpdateBlogPostDto } from './dto/update-blog-post.dto';
import { BlogPost, BlogPostDocument } from './entities/blog-post.entity';

@Injectable()
export class BlogPostService {
  constructor(
    @InjectModel(BlogPost.name) private blogPostModel: Model<BlogPostDocument>,
  ) {}

  async create(createBlogPostDto: CreateBlogPostDto): Promise<BlogPost> {
    const createdBlogPost = new this.blogPostModel(createBlogPostDto);
    return createdBlogPost.save();
  }

  async findAll(): Promise<BlogPost[]> {
    return this.blogPostModel.find().exec();
  }

  async findOne(id: string): Promise<BlogPost> {
    const blogPost = await this.blogPostModel.findById(id).exec();
    if (!blogPost) {
      throw new NotFoundException(`BlogPost with ID ${id} not found`);
    }
    return blogPost;
  }

  async findBySlug(slug: string): Promise<BlogPost> {
    const blogPost = await this.blogPostModel.findOne({ slug }).exec();
    if (!blogPost) {
      throw new NotFoundException(`BlogPost with slug ${slug} not found`);
    }
    return blogPost;
  }

  async update(
    id: string,
    updateBlogPostDto: UpdateBlogPostDto,
  ): Promise<BlogPost> {
    const updatedBlogPost = await this.blogPostModel
      .findByIdAndUpdate(id, updateBlogPostDto, { new: true })
      .exec();

    if (!updatedBlogPost) {
      throw new NotFoundException(`BlogPost with ID ${id} not found`);
    }

    return updatedBlogPost;
  }

  async remove(id: string): Promise<BlogPost> {
    const deletedBlogPost = await this.blogPostModel
      .findByIdAndDelete(id)
      .exec();

    if (!deletedBlogPost) {
      throw new NotFoundException(`BlogPost with ID ${id} not found`);
    }

    return deletedBlogPost;
  }
}
